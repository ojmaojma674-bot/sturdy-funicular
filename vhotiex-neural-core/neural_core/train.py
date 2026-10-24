import json
from pathlib import Path

import torch
import torch.nn as nn
import torch.optim as optim

from .model import DEFAULT_MODEL_PATH, VhotiexNeuralNetwork


def load_intents(data_path: str | Path = Path(__file__).resolve().parents[1] / "data" / "intents.json") -> list[str]:
    with Path(data_path).open("r", encoding="utf-8") as fh:
        payload = json.load(fh)
    return payload.get("intents", [])


def train_model(
    model: VhotiexNeuralNetwork | None = None,
    epochs: int = 50,
    model_path: str | Path = DEFAULT_MODEL_PATH,
    data_path: str | Path = Path(__file__).resolve().parents[1] / "data" / "intents.json",
):
    if model is None:
        model = VhotiexNeuralNetwork()

    intent_names = load_intents(data_path)
    output_size = len(intent_names)
    if output_size != model.network[-1].out_features:
        model = VhotiexNeuralNetwork(output_size=output_size)

    torch.manual_seed(42)
    inputs = torch.randn(200, 128)
    labels = torch.randint(0, output_size, (200,))

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch + 1}/{epochs} - loss={loss.item():.4f}")

    save_path = Path(model_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), save_path)
    print(f"Model saved to {save_path}")
    return model


if __name__ == "__main__":
    train_model()
