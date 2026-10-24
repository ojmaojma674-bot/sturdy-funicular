from pathlib import Path

import torch
import torch.nn as nn


class VhotiexNeuralNetwork(nn.Module):
    """A compact classifier for intent routing."""

    def __init__(self, input_size: int = 128, hidden_size: int = 256, output_size: int = 10):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


DEFAULT_MODEL_PATH = Path(__file__).resolve().parents[1] / "artifacts" / "vhotiex_model.pt"


def load_model(model_path: str | Path = DEFAULT_MODEL_PATH) -> VhotiexNeuralNetwork:
    model = VhotiexNeuralNetwork()
    path = Path(model_path)
    if not path.exists():
        raise FileNotFoundError(f"Model not found at {path}")
    model.load_state_dict(torch.load(path, map_location="cpu"))
    model.eval()
    return model
