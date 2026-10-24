from pathlib import Path

import torch

from .model import VhotiexNeuralNetwork, load_model
from .train import load_intents


def predict_intent(features: list[float], model_path: str | Path = Path(__file__).resolve().parents[1] / "artifacts" / "vhotiex_model.pt") -> dict:
    model = load_model(model_path)
    tensor = torch.tensor(features, dtype=torch.float32).reshape(1, -1)

    with torch.no_grad():
        logits = model(tensor)
        predicted_index = int(logits.argmax(dim=1).item())

    intent_names = load_intents()
    label = intent_names[predicted_index] if predicted_index < len(intent_names) else "unknown"

    return {
        "predicted_index": predicted_index,
        "intent": label,
        "confidence": float(torch.softmax(logits, dim=1).max().item()),
    }


if __name__ == "__main__":
    sample = [0.0] * 128
    print(predict_intent(sample))
