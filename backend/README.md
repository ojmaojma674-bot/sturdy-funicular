# VHOTIEX AI Backend

This backend provides the FastAPI API for the VHOTIEX AI assistant, including chat routing and agent metadata.

## Local setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

## Available endpoints

- `GET /` — health check
- `POST /chat/` — send a message to the agent routing flow
- `GET /agents/` — list all supported agents
- `GET /agents/{agent_name}` — fetch agent profile details

## Notes

- The backend is intentionally lightweight and uses in-memory routing logic.
- Add your real model provider keys and implementation as the project grows.
