from __future__ import annotations

from pathlib import Path

import torch

from neural_core.model import VhotiexNeuralNetwork
from neural_core.train import train_model


def test_model_output_shape():
    model = VhotiexNeuralNetwork()
    x = torch.randn(4, 128)
    output = model(x)
    assert output.shape == (4, 10)


def test_training_creates_model_file(tmp_path):
    model_path = tmp_path / "test_model.pt"
    model = train_model(model_path=model_path, epochs=5)
    assert model is not None
    assert Path(model_path).exists()


def test_predict_intent_returns_valid_shape():
    sample = [0.0] * 128
    prediction = __import__("neural_core.predict", fromlist=["predict_intent"]).predict_intent(sample)
    assert "intent" in prediction
    assert "confidence" in prediction
    assert 0.0 <= prediction["confidence"] <= 1.0
