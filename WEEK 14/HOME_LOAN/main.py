import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
from typing import Literal

# 1. Initialize FastAPI app
app = FastAPI(title="Home Loan Approval API",
              description="API to predict home loan approval (Approved/Rejected).",
              version="1.0")

# 2. Load the saved model, scaler, encoders, and features
try:
    model = joblib.load('home_loan_model.joblib')
    scaler = joblib.load('home_loan_scaler.joblib')
    encoders = joblib.load('home_loan_encoders.joblib')
    feature_names = joblib.load('home_loan_features.joblib')
    print("Model, scaler, encoders, and features loaded successfully.")
except Exception as e:
    print(f"Error loading files: {e}")
    model = None
    scaler = None
    encoders = None
    feature_names = None


# 3. Define the input data model using Pydantic
class LoanApplication(BaseModel):
    Gender: Literal['Male', 'Female']
    Married: Literal['Yes', 'No']
    Dependents: Literal['0', '1', '2', '3+']
    Education: Literal['Graduate', 'Not Graduate']
    Self_Employed: Literal['Yes', 'No']
    ApplicantIncome: int
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float = Field(..., description="1.0 for history exists, 0.0 for not")
    Property_Area: Literal['Urban', 'Semiurban', 'Rural']

    class Config:
        json_schema_extra = {
            "example": {
                "Gender": "Male",
                "Married": "Yes",
                "Dependents": "1",
                "Education": "Graduate",
                "Self_Employed": "No",
                "ApplicantIncome": 4583,
                "CoapplicantIncome": 1508.0,
                "LoanAmount": 128.0,
                "Loan_Amount_Term": 360.0,
                "Credit_History": 1.0,
                "Property_Area": "Rural"
            }
        }


# 4. Define helper function for preprocessing
def preprocess_input(features: LoanApplication):
    # Create a dictionary from the input
    data = features.dict()
    df = pd.DataFrame([data])

    # Label Encoding for categorical categories
    for col, encoder in encoders.items():
        try:
            input_val = df.at[0, col]
            df.at[0, col] = encoder.transform([input_val])[0]
        except ValueError:
            # Handle unseen category (e.g., if user inputs '4' for Dependents)
            df.at[0, col] = 0  # Default to 0

    # Scale numeric features
    numeric_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
    df[numeric_cols] = scaler.transform(df[numeric_cols])

    # Ensure all columns are numeric
    df = df.astype(float)

    # Reorder columns to match training order
    df = df[feature_names]

    return df


# 5. Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Home Loan Approval Prediction API. Go to /docs for details."}


# 6. Define the prediction endpoint
@app.post("/predict/")
def predict_status(features: LoanApplication):
    """
    Predicts the home loan approval status (Approved or Rejected).

    - **features**: A JSON object with applicant details.
    - **returns**: A JSON object with the prediction ("Approved" or "Rejected").
    """
    if not all([model, scaler, encoders, feature_names]):
        return {"error": "Model or supporting files not loaded. Please run the notebook to generate .joblib files."}

    # Preprocess the raw input data
    processed_data = preprocess_input(features)

    # Make prediction
    prediction_numeric = model.predict(processed_data)

    # Get probability of "Approved" (class 1)
    try:
        probability_approved = model.predict_proba(processed_data)[0][1]
    except:
        probability_approved = "N/A"

    # Convert numeric prediction (0 or 1)
    prediction_label = "Approved" if prediction_numeric[0] == 1 else "Rejected"

    return {
        "prediction": prediction_label,
        "prediction_value": int(prediction_numeric[0]),
        "probability_approved": float(probability_approved)
    }


# 7. Run the API server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)