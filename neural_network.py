from pathlib import Path

import torch
import torch.nn as nn
import torch.optim as optim

MODEL_PATH = Path(__file__).with_name("vhotiex_model.pt")


class VhotiexNeuralNetwork(nn.Module):
    def __init__(self, input_size=128, hidden_size=256, output_size=10):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, x):
        return self.network(x)


def train_model(model, inputs, labels, epochs=100):
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
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item():.4f}")

    model_path = MODEL_PATH
    torch.save(model.state_dict(), model_path)
    print(f"Model saved successfully to {model_path}")
    return model_path


def ensure_model(model: VhotiexNeuralNetwork, *, force_retrain: bool = False):
    if force_retrain or not MODEL_PATH.exists():
        torch.manual_seed(42)
        x = torch.randn(200, 128)
        y = torch.randint(0, 10, (200,))
        train_model(model, x, y)
        return model

    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    return model


if __name__ == "__main__":
    torch.manual_seed(42)
    model = VhotiexNeuralNetwork()
    ensure_model(model)
    print("VHOTIEX Neural Core ready.")
