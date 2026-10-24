from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from backend.config import get_settings
from backend.security import validate_feature_vector
from neural_core.predict import predict_intent

app = FastAPI(title="VHOTIEX Neural Core")
settings = get_settings()


class PredictionPayload(BaseModel):
    features: list[float]


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.app_env,
    }


@app.post("/predict")
def predict(payload: PredictionPayload) -> dict:
    features = validate_feature_vector(payload.features)
    result = predict_intent(features)
    return {
        "status": "accepted",
        "prediction": result,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.api_host, port=settings.api_port)
