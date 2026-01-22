import joblib
import numpy as np

MODEL_PATH = "model/model.pkl"

model = joblib.load(MODEL_PATH)

def predict(features: list):
    if len(features) != 4:
        raise ValueError(f"Expected 4 features, got {len(features)}")
    data = np.array(features).reshape(1, -1)
    prediction = model.predict(data)
    return int(prediction[0])
