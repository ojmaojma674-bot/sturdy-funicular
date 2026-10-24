from fastapi import APIRouter
from pydantic import BaseModel, Field

from backend.services.ml_service import LinearRegressionPredictor, LogisticRegressionPredictor

router = APIRouter(prefix="/ml", tags=["ml"])

linear_predictor = LinearRegressionPredictor()
logistic_predictor = LogisticRegressionPredictor()


class LinearRegressionRequest(BaseModel):
    room_size: float = Field(..., gt=0)


class LogisticRegressionRequest(BaseModel):
    study_hours: float = Field(..., ge=0)
    attendance: float = Field(..., ge=0, le=100)


@router.get("/status")
def ml_status() -> dict:
    return {
        "status": "ready",
        "models": ["linear_regression", "logistic_regression"],
    }


@router.post("/linear-regression/predict")
def predict_linear_regression(payload: LinearRegressionRequest) -> dict:
    prediction = linear_predictor.predict(payload.room_size)
    return {
        "model": "linear_regression",
        "input": {"room_size": payload.room_size},
        "predicted_value": round(float(prediction), 2),
    }


@router.post("/logistic-regression/predict")
def predict_logistic_regression(payload: LogisticRegressionRequest) -> dict:
    result = logistic_predictor.predict(payload.study_hours, payload.attendance)
    return {
        "model": "logistic_regression",
        "input": {
            "study_hours": payload.study_hours,
            "attendance": payload.attendance,
        },
        "prediction": result["label"],
        "probability": round(float(result["probability"]), 4),
        "binary_prediction": result["prediction"],
    }
