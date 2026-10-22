from fastapi import FastAPI

app = FastAPI(title="Vhotiex AI API", version="0.1.0")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "vhotiex-ai"}
