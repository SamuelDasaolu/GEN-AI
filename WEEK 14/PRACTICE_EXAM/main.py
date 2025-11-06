import uvicorn
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# --- 1. Load Model, Scaler, and Feature List ---
try:
    model = joblib.load('easy_visa_model.pkl')
    scaler = joblib.load('easy_visa_scaler.pkl')
    model_features = joblib.load('easy_visa_features.pkl')
except FileNotFoundError:
    print("--- FATAL ERROR ---")
    print("Model/scaler/feature files not found.") # Run final Cell of Notebook to Create them first
    exit()

# --- 2. Define API and Input/Output Schemas ---
app = FastAPI(
    title="Easy Visa Prediction API",
    description="Predicts visa certification status (Certified/Denied)."
)


class VisaApplication(BaseModel):
    """Defines the raw input from the user."""
    continent: str
    education_of_employee: str
    has_job_experience: str
    requires_job_training: str
    no_of_employees: int
    yr_of_estab: int
    region_of_employment: str
    prevailing_wage: float
    unit_of_wage: str
    full_time_position: str

    class Config:
        json_schema_extra = {
            "example": {
                "continent": "Asia",
                "education_of_employee": "Master's",
                "has_job_experience": "Y",
                "requires_job_training": "N",
                "no_of_employees": 14513,
                "yr_of_estab": 2007,
                "region_of_employment": "West",
                "prevailing_wage": 592.2029,
                "unit_of_wage": "Hour",
                "full_time_position": "Y"
            }
        }


class PredictionResponse(BaseModel):
    """Defines the API's JSON response."""
    prediction: str
    confidence: str
    probabilities: dict


# --- 3. Helper and Preprocessing Functions ---

def _calculate_annual_wage(wage: float, unit: str) -> float:
    """Pure function to convert any wage to an annual wage."""
    if unit == 'Year':
        return wage
    if unit == 'Month':
        return wage * 12
    if unit == 'Week':
        return wage * 52
    if unit == 'Hour':
        return wage * 40 * 52  # Assuming 40-hour week
    return wage


def preprocess_input(data: VisaApplication, model_cols: List[str]) -> pd.DataFrame:
    """
    Takes raw VisaApplication data and returns a single-row,
    scaled DataFrame ready for the model.
    """
    # 1. Create a dictionary for the engineered/mapped features
    feature_dict = {
        'has_job_experience': 1 if data.has_job_experience == 'Y' else 0,
        'requires_job_training': 1 if data.requires_job_training == 'Y' else 0,
        'full_time_position': 1 if data.full_time_position == 'Y' else 0,
        'no_of_employees': data.no_of_employees,
        'annual_wage': _calculate_annual_wage(data.prevailing_wage, data.unit_of_wage),
        'company_age': 2016 - data.yr_of_estab  # Using 2016 as reference year
    }

    # 2. Initialize the feature-ready DataFrame
    # This creates a DataFrame with one row of zeros
    # and all the exact columns the model expects.
    api_df = pd.DataFrame(columns=model_cols)
    api_df.loc[0] = 0

    # 3. Fill in the values from our dictionary
    for col, value in feature_dict.items():
        if col in api_df.columns:
            api_df.at[0, col] = value

    # 4. Handle the one-hot encoded features
    # This is a robust way to set the right dummy variable to 1
    ohe_prefixes = ['continent_', 'education_of_employee_', 'region_of_employment_']
    user_inputs = [data.continent, data.education_of_employee, data.region_of_employment]

    for prefix, user_input in zip(ohe_prefixes, user_inputs):
        col_name = f"{prefix}{user_input}"
        if col_name in api_df.columns:
            api_df.at[0, col_name] = 1

    # 5. Scale the numerical features
    numerical_cols = ['no_of_employees', 'company_age', 'annual_wage']
    api_df[numerical_cols] = scaler.transform(api_df[numerical_cols])

    # Ensure column order matches the model's training
    return api_df[model_cols]


# --- 4. API Endpoints ---

@app.get("/")
def read_root():
    """Root endpoint with a welcome message."""
    return {"message": "Welcome to the Easy Visa Prediction API. Go to /docs to test."}


@app.post("/predict", response_model=PredictionResponse)
def predict_visa(application: VisaApplication):
    """
    Takes application data and returns a Certified/Denied prediction.
    """
    # 1. Preprocess the raw input
    processed_df = preprocess_input(application, model_features)

    # 2. Make prediction and get probabilities
    prediction = model.predict(processed_df)[0]
    probabilities = model.predict_proba(processed_df)[0]

    # 3. Format the response
    status = "Certified" if prediction == 1 else "Denied"
    confidence = probabilities[prediction]

    return {
        "prediction": status,
        "confidence": f"{confidence:.2%}",
        "probabilities": {
            "Denied": f"{probabilities[0]:.2%}",
            "Certified": f"{probabilities[1]:.2%}"
        }
    }


# --- 5. Run the App ---
if __name__ == "__main__":
    # You would run this from your terminal with:
    # uvicorn main:app --reload
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)