from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/")
def chat_post(payload: dict) -> dict:
    return {
        "status": "accepted",
        "message": payload.get("message", ""),
        "response": "This is the starter message response for the VHOTIEX AI backend."
    }
