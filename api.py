from __future__ import annotations

import torch
from fastapi import FastAPI
from pydantic import BaseModel

from neural_network import VhotiexNeuralNetwork, ensure_model

app = FastAPI(title="VHOTIEX Neural Core")

model = VhotiexNeuralNetwork()
ensure_model(model)


class PredictionRequest(BaseModel):
    features: list[float]


@app.get("/")
def home():
    return {"name": "VHOTIEX Neural Core", "status": "online"}


@app.post("/predict")
def predict(request: PredictionRequest):
    if len(request.features) != 128:
        return {"error": "Exactly 128 features required"}

    tensor = torch.tensor(request.features, dtype=torch.float32).reshape(1, 128)

    with torch.no_grad():
        result = model(tensor)
        prediction = int(result.argmax(dim=1).item())

    return {"prediction": prediction}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=False)
