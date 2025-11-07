import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from typing import Literal

# 1. Initialize FastAPI app
app = FastAPI(title="German Credit Risk API",
              description="API to predict credit risk (Good/Bad) based on applicant details.",
              version="1.0")

# 2. Load the saved model, scaler, encoders, and features
try:
    model = joblib.load('german_credit_model.joblib')
    scaler = joblib.load('german_credit_scaler.joblib')
    encoders = joblib.load('german_credit_encoders.joblib')
    feature_names = joblib.load('german_credit_features.joblib')
    print("Model, scaler, encoders, and features loaded successfully.")
except Exception as e:
    print(f"Error loading files: {e}")
    model = None
    scaler = None
    encoders = None
    feature_names = None


# 3. Define the input data model using Pydantic
# We use the raw string values for simplicity, as requested.
class CreditApplicant(BaseModel):
    Age: int
    Sex: Literal['male', 'female']
    Job: Literal['unskilled and non-resident', 'unskilled and resident', 'skilled', 'highly skilled']
    Housing: Literal['own', 'rent', 'free']
    Saving_accounts: Literal['little', 'moderate', 'quite rich', 'rich']
    Checking_account: Literal['little', 'moderate', 'rich']
    Credit_amount: int
    Duration: int
    Purpose: Literal[
        'car', 'furniture/equipment', 'radio/TV', 'domestic appliances', 'repairs', 'education', 'business', 'vacation/others']

    class Config:
        json_schema_extra = {
            "example": {
                "Age": 45,
                "Sex": "male",
                "Job": "skilled",
                "Housing": "free",
                "Saving_accounts": "little",
                "Checking_account": "little",
                "Credit_amount": 7882,
                "Duration": 42,
                "Purpose": "furniture/equipment"
            }
        }


# 4. Define helper function for preprocessing
def preprocess_input(features: CreditApplicant):
    # Create a dictionary from the input
    data = features.dict()

    # Rename keys to match dataframe columns
    data['Saving accounts'] = data.pop('Saving_accounts')
    data['Checking account'] = data.pop('Checking_account')
    data['Credit amount'] = data.pop('Credit_amount')

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Manual Ordinal Mapping
    savings_map = {'little': 0, 'moderate': 1, 'quite rich': 2, 'rich': 3}
    checking_map = {'little': 0, 'moderate': 1, 'rich': 2}
    job_map = {'unskilled and non-resident': 0, 'unskilled and resident': 1, 'skilled': 2, 'highly skilled': 3}

    df['Saving accounts'] = df['Saving accounts'].map(savings_map)
    df['Checking account'] = df['Checking account'].map(checking_map)
    df['Job'] = df['Job'].map(job_map)

    # Label Encoding for nominal categories
    for col, encoder in encoders.items():
        # Use .transform() on the loaded encoder
        # We handle unknown categories by assigning -1 and later filling with 0
        try:
            df[col] = encoder.transform(df[col])
        except ValueError:
            df[col] = 0  # Default to most common category if unseen

    # Scale numeric features
    numeric_cols = ['Age', 'Credit amount', 'Duration']
    df[numeric_cols] = scaler.transform(df[numeric_cols])

    # Ensure column order matches training
    df = df[feature_names]

    return df


# 5. Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the German Credit Risk Prediction API. Go to /docs for details."}


# 6. Define the prediction endpoint
@app.post("/predict/")
def predict_risk(features: CreditApplicant):
    """
    Predicts the credit risk (Good or Bad) given applicant features.

    - **features**: A JSON object with applicant details.
    - **returns**: A JSON object with the prediction ("Good Risk" or "Bad Risk").
    """
    if not all([model, scaler, encoders, feature_names]):
        return {"error": "Model or supporting files not loaded. Please run the notebook to generate .joblib files."}

    # Preprocess the raw input data
    processed_data = preprocess_input(features)

    # Make prediction
    prediction_numeric = model.predict(processed_data)

    # Get probability of "Bad Risk" (class 1)
    try:
        probability_bad_risk = model.predict_proba(processed_data)[0][1]
    except:
        probability_bad_risk = "N/A"  # Some models might not have predict_proba

    # Convert numeric prediction (0 or 1) to "Good Risk" or "Bad Risk"
    prediction_label = "Good Risk" if prediction_numeric[0] == 0 else "Bad Risk"

    return {
        "prediction": prediction_label,
        "prediction_value": int(prediction_numeric[0]),
        "probability_bad_risk": float(probability_bad_risk)
    }


# 7. Run the API server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)