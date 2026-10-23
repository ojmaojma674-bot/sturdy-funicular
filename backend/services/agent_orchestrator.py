"""API routes for chat requests and agent routing."""

from fastapi import APIRouter

from backend.services.agent_orchestrator import AgentOrchestrator
from backend.services.model_router import ModelRouter

router = APIRouter(prefix="/chat", tags=["chat"])

orchestrator = AgentOrchestrator(ModelRouter())
ALLOWED_AGENTS = {
    "Astra",
    "Nova",
    "Lyra",
    "Orion",
    "Echo",
    "Sable",
    "Kite",
    "Quill",
}


@router.post("/")
def chat_post(payload: dict) -> dict:
    """Route a chat payload to the best agent and return a response."""
    user_message = str(payload.get("message", "")).strip()
    selected_agent = str(payload.get("agent", "Astra")).strip() or "Astra"

    if not user_message:
        return {
            "status": "empty",
            "message": "",
            "response": (
                "Tell me what you want help with and I will route it to the best "
                "agent."
            ),
            "agent": selected_agent,
        }

    plan = orchestrator.build_response_plan(user_message)
    agent_name = (
        selected_agent
        if selected_agent in ALLOWED_AGENTS
        else plan["agent"]
    )
    profile = orchestrator.swarm.profile_for(agent_name)

    response_text = (
        f"{agent_name} here. I am handling this in {profile.role if profile else 'team'} "
        "mode. I will focus on "
        f"{profile.specialties[0] if profile and profile.specialties else 'smart assistance'} "
        "while keeping the response clear and human-friendly."
    )

    return {
        "status": "accepted",
        "message": user_message,
        "agent": agent_name,
        "model": plan["model"],
        "role": profile.role if profile else "General",
        "response": response_text,
        "personality": profile.to_dict() if profile else {},
    }
