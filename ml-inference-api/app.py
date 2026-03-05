from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Flower label mapping
label_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

# Create FastAPI instance
app = FastAPI()

# Define input data format
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "ML Inference API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: IrisInput):

    input_array = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction = model.predict(input_array)[0]

    flower_name = label_map[int(prediction)]

    return {
        "prediction": flower_name
    }
    return {"prediction": int(prediction[0])}
