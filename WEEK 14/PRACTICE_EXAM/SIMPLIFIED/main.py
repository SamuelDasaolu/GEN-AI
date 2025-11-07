import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from typing import Literal

# 1. Initialize FastAPI app
app = FastAPI(title="EasyVisa Prediction API",
              description="API to predict visa application status (Certified/Denied).",
              version="1.0")

# 2. Load the saved model, scaler, encoders, and features
try:
    model = joblib.load('easy_visa_model.joblib')
    scaler = joblib.load('easy_visa_scaler.joblib')
    encoders = joblib.load('easy_visa_encoders.joblib')
    feature_names = joblib.load('easy_visa_features.joblib')
    print("Model, scaler, encoders, and features loaded successfully.")
except Exception as e:
    print(f"Error loading files: {e}")
    model = None
    scaler = None
    encoders = None
    feature_names = None


# 3. Define the input data model using Pydantic
class VisaApplication(BaseModel):
    continent: Literal['Asia', 'Africa', 'North America', 'Europe', 'South America', 'Oceania']
    education_of_employee: Literal["Master's", 'High School', "Bachelor's", 'Doctorate']
    has_job_experience: Literal['Y', 'N']
    requires_job_training: Literal['Y', 'N']
    no_of_employees: int
    yr_of_estab: int
    prevailing_wage: float
    region_of_employment: Literal['South', 'Northeast', 'Asia', 'West', 'Midwest', 'Island', 'All']
    unit_of_wage: Literal['Hour', 'Year', 'Week', 'Month']
    full_time_position: Literal['Y', 'N']

    class Config:
        json_schema_extra = {
            "example": {
                "continent": "Asia",
                "education_of_employee": "Master's",
                "has_job_experience": "Y",
                "requires_job_training": "N",
                "no_of_employees": 1008,
                "yr_of_estab": 2006,
                "prevailing_wage": 10343.5,
                "region_of_employment": "Northeast",
                "unit_of_wage": "Year",
                "full_time_position": "Y"
            }
        }


# 4. Define helper function for preprocessing
def preprocess_input(features: VisaApplication):
    # Create a dictionary from the input
    data = features.dict()
    df = pd.DataFrame([data])

    # Label Encoding for categorical categories
    for col, encoder in encoders.items():
        try:
            # Get the input value for the column
            input_val = df.at[0, col]
            # Transform it
            df.at[0, col] = encoder.transform([input_val])[0]
        except ValueError:
            # Handle unseen category by mapping to 0
            df.at[0, col] = 0

            # Ensure all columns are numeric
    df = df.astype(float)

    # Reorder columns to match training order
    df = df[feature_names]

    # Scale the features
    scaled_data = scaler.transform(df)

    return scaled_data


# 5. Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the EasyVisa Prediction API. Go to /docs for details."}


# 6. Define the prediction endpoint
@app.post("/predict/")
def predict_status(features: VisaApplication):
    """
    Predicts the visa case status (Certified or Denied).

    - **features**: A JSON object with applicant details.
    - **returns**: A JSON object with the prediction ("Certified" or "Denied").
    """
    if not all([model, scaler, encoders, feature_names]):
        return {"error": "Model or supporting files not loaded. Please run the notebook to generate .joblib files."}

    # Preprocess the raw input data
    processed_data = preprocess_input(features)

    # Make prediction
    prediction_numeric = model.predict(processed_data)

    # Get probability of "Certified" (class 1)
    try:
        probability_certified = model.predict_proba(processed_data)[0][1]
    except:
        probability_certified = "N/A"

    # Convert numeric prediction (0 or 1)
    prediction_label = "Certified" if prediction_numeric[0] == 1 else "Denied"

    return {
        "prediction": prediction_label,
        "prediction_value": int(prediction_numeric[0]),
        "probability_certified": float(probability_certified)
    }


# 7. Run the API server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)