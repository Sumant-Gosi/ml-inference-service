from fastapi import FastAPI, HTTPException
from app.schema import PredictionRequest, PredictionResponse
from app.model import predict

app = FastAPI(title="ML Inference Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict_endpoint(request: PredictionRequest):
    try:
        prediction = predict(request.features)
        return {"prediction": prediction}
    except ValueError as e:
        # Convert ValueError to HTTP 400
        raise HTTPException(status_code=400, detail=str(e))
