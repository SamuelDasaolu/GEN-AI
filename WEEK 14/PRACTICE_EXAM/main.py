import uvicorn
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# --- 1. Initialize FastAPI App ---
app = FastAPI(
    title="Easy Visa Prediction API",
    description="An API to predict visa certification status based on application details.",
    version="1.0"
)

# --- 2. Load Model, Scaler, and Features ---
# These files MUST be in the same directory as this script.
try:
    model = joblib.load('easy_visa_model.joblib')
    scaler = joblib.load('easy_visa_scaler.joblib')
    # Load the exact feature names the model was trained on
    model_features = joblib.load('easy_visa_features.joblib')
except Exception as e:
    print(f"Error loading model/scaler: {e}")
    print(
        "Please make sure 'easy_visa_model.joblib', 'easy_visa_scaler.joblib', and 'easy_visa_features.joblib' are in the same directory.")
    model, scaler, model_features = None, None, []


# --- 3. Define Input Schema (Pydantic Model) ---
# This defines the data structure for the API request.
# We use the ORIGINAL features, before preprocessing.
class VisaApplication(BaseModel):
    continent: str
    education_of_employee: str
    has_job_experience: str  # 'Y' or 'N'
    requires_job_training: str  # 'Y' or 'N'
    no_of_employees: int
    yr_of_estab: int
    region_of_employment: str
    prevailing_wage: float
    unit_of_wage: str  # 'Hour', 'Week', 'Month', 'Year'
    full_time_position: str  # 'Y' or 'N'

    # Example for testing in the /docs UI
    class Config:
        schema_extra = {
            "example": {
                "continent": "Asia",
                "education_of_employee": "Master's",
                "has_job_experience": "Y",
                "requires_job_training": "N",
                "no_of_employees": 2412,
                "yr_of_estab": 2002,
                "region_of_employment": "Northeast",
                "prevailing_wage": 83425.65,
                "unit_of_wage": "Year",
                "full_time_position": "Y"
            }
        }


# --- 4. Preprocessing Function ---
def preprocess_input(data: VisaApplication) -> pd.DataFrame:
    """
    Transforms the raw input from the API into the
    18-feature, scaled format the model expects.
    """

    # --- Feature Engineering (Task 3.1) ---

    # 1. Create Annual Wage
    annual_wage = 0
    if data.unit_of_wage == 'Year':
        annual_wage = data.prevailing_wage
    elif data.unit_of_wage == 'Month':
        annual_wage = data.prevailing_wage * 12
    elif data.unit_of_wage == 'Week':
        annual_wage = data.prevailing_wage * 52
    elif data.unit_of_wage == 'Hour':
        annual_wage = data.prevailing_wage * 40 * 52

    # 2. Create Company Age
    # Assuming 2016 as the reference year from the project
    company_age = 2016 - data.yr_of_estab

    # --- Encoding (Task 3.2) ---

    # 1. Create a dictionary for the raw data
    input_dict = {
        'has_job_experience': 1 if data.has_job_experience == 'Y' else 0,
        'requires_job_training': 1 if data.requires_job_training == 'N' else 0,
        'no_of_employees': data.no_of_employees,
        'full_time_position': 1 if data.full_time_position == 'Y' else 0,
        'annual_wage': annual_wage,
        'company_age': company_age
    }

    # 2. Create DataFrame for one-hot encoding
    # We create a new DataFrame with the model's features, all set to 0
    processed_df = pd.DataFrame(columns=model_features)
    processed_df.loc[0] = 0  # Initialize the first row with zeros

    # 3. Fill in the non-one-hot-encoded values
    for col, value in input_dict.items():
        if col in processed_df.columns:
            processed_df.at[0, col] = value

    # 4. Manually set the one-hot-encoded dummy variables
    # This is safer than pd.get_dummies on a single row

    # Continent
    continent_col = f"continent_{data.continent}"
    if continent_col in processed_df.columns:
        processed_df.at[0, continent_col] = 1

    # Education
    edu_col = f"education_of_employee_{data.education_of_employee}"
    if edu_col in processed_df.columns:
        processed_df.at[0, edu_col] = 1

    # Region
    region_col = f"region_of_employment_{data.region_of_employment}"
    if region_col in processed_df.columns:
        processed_df.at[0, region_col] = 1

    # --- Scaling (Task 3.3) ---
    numerical_features = ['no_of_employees', 'company_age', 'annual_wage']

    # Use the loaded scaler to transform the numerical features
    processed_df[numerical_features] = scaler.transform(processed_df[numerical_features])

    return processed_df


# --- 5. Prediction Endpoint ---
@app.post("/predict")
async def predict_visa_status(application: VisaApplication):
    """
    Predicts visa certification status.
    - **Input**: A JSON object with applicant and employer details.
    - **Output**: A JSON object with the prediction ('Certified' or 'Denied')
                 and the confidence probability.
    """
    if not all([model, scaler, model_features]):
        return {"error": "Model or scaler not loaded. Check server logs."}

    # 1. Preprocess the incoming data
    processed_data = preprocess_input(application)

    # 2. Make prediction
    prediction = model.predict(processed_data)[0]  # [0] to get the value
    probabilities = model.predict_proba(processed_data)[0]  # [0] to get probs

    # 3. Format the response
    status = "Certified" if prediction == 1 else "Denied"
    confidence = probabilities[prediction]  # Probability of the predicted class

    return {
        "prediction": status,
        "confidence": f"{confidence:.2%}",
        "class_probabilities": {
            "Denied": f"{probabilities[0]:.2%}",
            "Certified": f"{probabilities[1]:.2%}"
        }
    }


# --- 6. Root Endpoint ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Easy Visa Prediction API. Go to /docs to see the features."}


# --- 7. Run the App ---
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)