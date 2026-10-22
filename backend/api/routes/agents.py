from fastapi import APIRouter

router = APIRouter(prefix="/agents", tags=["agents"])


@router.get("/types")
def get_agent_types() -> dict:
    return {
        "agents": [
            "coding",
            "research",
            "analysis",
            "planning",
            "review",
            "voice",
            "memory"
        ]
    }
