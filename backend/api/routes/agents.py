"""API routes for agent discovery and metadata."""

from fastapi import APIRouter

from backend.services.agent_orchestrator import AgentOrchestrator
from backend.services.model_router import ModelRouter

router = APIRouter(prefix="/agents", tags=["agents"])

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


@router.get("/")
def get_agent_types() -> dict:
    """Return the full roster of agents and the default recommendation."""
    return {
        "agents": orchestrator.swarm.as_list(),
        "recommended_default": "Astra",
    }


@router.get("/{agent_name}")
def get_agent(agent_name: str) -> dict:
    """Return the metadata for a single agent profile."""
    profile = orchestrator.swarm.profile_for(agent_name)
    if profile is None:
        return {"error": "Agent not found", "agent_name": agent_name}
    return profile.to_dict()
