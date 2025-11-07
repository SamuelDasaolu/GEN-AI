import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# 1. Initialize FastAPI app
app = FastAPI(title="White Wine Quality Predictor API",
              description="An API to predict White Wine quality (Good/Bad) based on chemical features.",
              version="1.0")

# 2. Load the saved model and scaler
# Note: We are loading the 'white_wine' files
try:
    model = joblib.load('white_wine_model.joblib')
    scaler = joblib.load('white_wine_scaler.joblib')
    print("White wine model and scaler loaded successfully.")
except Exception as e:
    print(f"Error loading model/scaler: {e}")
    model = None
    scaler = None


# 3. Define the input data model using Pydantic
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

    # Example for API documentation (using a white wine example)
    class Config:
        json_schema_extra = {
            "example": {
                "fixed_acidity": 7.0,
                "volatile_acidity": 0.27,
                "citric_acid": 0.36,
                "residual_sugar": 20.7,
                "chlorides": 0.045,
                "free_sulfur_dioxide": 45.0,
                "total_sulfur_dioxide": 170.0,
                "density": 1.001,
                "pH": 3.0,
                "sulphates": 0.45,
                "alcohol": 8.8
            }
        }


# 4. Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the White Wine Quality Prediction API. Go to /docs for details."}


# 5. Define the prediction endpoint
@app.post("/predict/")
def predict_quality(features: WineFeatures):
    """
    Predicts the quality of a white wine (Good or Bad) given its features.

    - **features**: A JSON object with the 11 chemical features.
    - **returns**: A JSON object with the prediction ("Good" or "Bad").
    """
    if model is None or scaler is None:
        return {"error": "Model or scaler not loaded. Please run the notebook to generate .joblib files."}

    # Convert input data to a 2D array
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
    uvicorn.run(app, host="127.0.0.1", port=8000)