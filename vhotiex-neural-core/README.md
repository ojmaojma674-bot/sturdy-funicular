# VHOTIEX Neural Core

A lightweight neural intent engine and FastAPI backend for the VHOTIEX AI system.

## Project structure

- `neural_core/` contains the ML model and prediction logic.
- `backend/` contains the API layer and validation utilities.
- `data/` stores training or intent metadata.
- `tests/` contains basic verification for the model and prediction flow.

## Quick start

```bash
cd vhotiex-neural-core
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m neural_core.train
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints

- `GET /health` returns backend health
- `POST /predict` accepts a feature vector and returns the predicted intent label

## Notes

This is a clean starter scaffold intended for experimentation and iteration. Replace the synthetic training data with your production dataset as your model grows.
