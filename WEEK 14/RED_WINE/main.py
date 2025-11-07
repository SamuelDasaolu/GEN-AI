import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# 1. Initialize FastAPI app
app = FastAPI(title="Wine Quality Predictor API",
              description="An API to predict Red Wine quality (Good/Bad) based on chemical features.",
              version="1.0")

# 2. Load the saved model and scaler
try:
    model = joblib.load('wine_model.joblib')
    scaler = joblib.load('wine_scaler.joblib')
    print("Model and scaler loaded successfully.")
except Exception as e:
    print(f"Error loading model/scaler: {e}")
    model = None
    scaler = None


# 3. Define the input data model using Pydantic
# These are the 11 features our model was trained on
class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

    # Example for API documentation
    class Config:
        json_schema_extra = {
            "example": {
                "fixed_acidity": 7.4,
                "volatile_acidity": 0.7,
                "citric_acid": 0.0,
                "residual_sugar": 1.9,
                "chlorides": 0.076,
                "free_sulfur_dioxide": 11.0,
                "total_sulfur_dioxide": 34.0,
                "density": 0.9978,
                "pH": 3.51,
                "sulphates": 0.56,
                "alcohol": 9.4
            }
        }


# 4. Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Wine Quality Prediction API. Go to /docs for details."}


# 5. Define the prediction endpoint
@app.post("/predict/")
def predict_quality(features: WineFeatures):
    """
    Predicts the quality of a wine (Good or Bad) given its features.

    - **features**: A JSON object with the 11 chemical features.
    - **returns**: A JSON object with the prediction ("Good" or "Bad").
    """
    if model is None or scaler is None:
        return {"error": "Model or scaler not loaded. Please run the notebook to generate .joblib files."}

    # Convert input data to a DataFrame (or 2D array)
    # The scaler expects a 2D array, so we use [[]]
    input_data = np.array([[
        features.fixed_acidity,
        features.volatile_acidity,
        features.citric_acid,
        features.residual_sugar,
        features.chlorides,
        features.free_sulfur_dioxide,
        features.total_sulfur_dioxide,
        features.density,
        features.pH,
        features.sulphates,
        features.alcohol
    ]])

    # Scale the input data
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction_numeric = model.predict(input_scaled)

    # Convert numeric prediction (0 or 1) to "Bad" or "Good"
    prediction_label = "Good" if prediction_numeric[0] == 1 else "Bad"

    return {"prediction": prediction_label, "prediction_value": int(prediction_numeric[0])}


# 6. Run the API server
if __name__ == "__main__":
    # This allows you to run the script directly with `python app.py`
    # and it will start the uvicorn server
    uvicorn.run(app, host="127.0.0.1", port=8000)