from fastapi import FastAPI
from backend.api.routes.agents import router as agents_router
from backend.api.routes.chat import router as chat_router

app = FastAPI(title="VHOTIEX AI Backend", version="0.1.0")

app.include_router(chat_router)
app.include_router(agents_router)

@app.get("/")
def root() -> dict:
    return {
        "name": "VHOTIEX AI",
        "status": "running",
        "version": "0.1.0"
    }
