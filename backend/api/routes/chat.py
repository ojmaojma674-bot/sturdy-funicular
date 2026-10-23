from fastapi import APIRouter

from backend.services.agent_orchestrator import AgentOrchestrator
from backend.services.llm_service import LLMService
from backend.services.model_router import ModelRouter

router = APIRouter(prefix="/chat", tags=["chat"])

orchestrator = AgentOrchestrator(ModelRouter())
llm_service = LLMService()


@router.post("/")
def chat_post(payload: dict) -> dict:
    user_message = str(payload.get("message", "")).strip()
    selected_agent = str(payload.get("agent", "Astra")).strip() or "Astra"

    if not user_message:
        return {
            "status": "empty",
            "message": "",
            "response": "Tell me what you want help with and I will route it to the best agent.",
            "agent": selected_agent,
        }

    plan = orchestrator.build_response_plan(user_message)
    allowed_agents = {"Astra", "Nova", "Lyra", "Orion", "Echo", "Sable", "Kite", "Quill"}
    agent_name = selected_agent if selected_agent in allowed_agents else plan["agent"]
    profile = orchestrator.swarm.profile_for(agent_name)

    response_text = llm_service.generate_response(user_message, agent_name=agent_name)

    return {
        "status": "accepted",
        "message": user_message,
        "agent": agent_name,
        "model": plan["model"],
        "role": profile.role if profile else "General",
        "response": response_text,
        "personality": profile.to_dict() if profile else {},
        "llm_enabled": llm_service.enabled,
    }
