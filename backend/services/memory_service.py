"""Agent orchestration primitives for routing prompts to specialty profiles."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentProfile:
    """Represent a single AI agent and the traits it uses for routing."""

    name: str
    role: str
    tone: str
    energy: str
    empathy: float
    reliability: float
    specialties: List[str] = field(default_factory=list)
    collaborators: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the profile as a dictionary for API responses."""
        return {
            "name": self.name,
            "role": self.role,
            "tone": self.tone,
            "energy": self.energy,
            "empathy": self.empathy,
            "reliability": self.reliability,
            "specialties": self.specialties,
            "collaborators": self.collaborators,
        }


class AgentSwarm:
    """Static collection of agent profiles used to describe the team."""

    def __init__(self, total_agents: int = 1_000_000):
        self.total_agents = total_agents
        self.agents = [
            AgentProfile(
                name="Astra",
                role="Coordinator",
                tone="calm and visionary",
                energy="steady",
                empathy=0.93,
                reliability=0.97,
                specialties=["planning", "alignment", "handoff"],
                collaborators=["Nova", "Lyra", "Orion"],
            ),
            AgentProfile(
                name="Nova",
                role="Researcher",
                tone="curious and precise",
                energy="high",
                empathy=0.82,
                reliability=0.9,
                specialties=["research", "analysis", "fact-checking"],
                collaborators=["Astra", "Quill", "Echo"],
            ),
            AgentProfile(
                name="Lyra",
                role="Composer",
                tone="creative and warm",
                energy="sparkling",
                empathy=0.94,
                reliability=0.88,
                specialties=["writing", "storytelling", "UX copy"],
                collaborators=["Astra", "Sable", "Kite"],
            ),
            AgentProfile(
                name="Orion",
                role="Engineer",
                tone="structured and effective",
                energy="focused",
                empathy=0.76,
                reliability=0.98,
                specialties=["code", "debugging", "systems"],
                collaborators=["Nova", "Echo", "Astra"],
            ),
            AgentProfile(
                name="Echo",
                role="Communicator",
                tone="empathetic and intuitive",
                energy="adaptive",
                empathy=0.96,
                reliability=0.9,
                specialties=["conversation", "translation", "support"],
                collaborators=["Lyra", "Nova", "Sable"],
            ),
            AgentProfile(
                name="Sable",
                role="Reviewer",
                tone="honest and sharp",
                energy="balanced",
                empathy=0.8,
                reliability=0.96,
                specialties=["quality assurance", "risk review", "policies"],
                collaborators=["Astra", "Orion", "Echo"],
            ),
            AgentProfile(
                name="Kite",
                role="Planner",
                tone="optimistic and strategic",
                energy="measured",
                empathy=0.87,
                reliability=0.94,
                specialties=["roadmaps", "priorities", "execution"],
                collaborators=["Astra", "Orion", "Lyra"],
            ),
            AgentProfile(
                name="Quill",
                role="Analyst",
                tone="thoughtful and detail-rich",
                energy="deep",
                empathy=0.83,
                reliability=0.92,
                specialties=["data", "patterns", "insights"],
                collaborators=["Nova", "Kite", "Sable"],
            ),
        ]

    def profile_for(self, name: str) -> Optional[AgentProfile]:
        """Return the matching profile for a given name, if available."""
        for agent in self.agents:
            if agent.name.lower() == name.lower():
                return agent
        return None

    def as_list(self) -> List[Dict[str, Any]]:
        """Serialize the swarm into a list of dictionaries."""
        return [agent.to_dict() for agent in self.agents]

    def summary(self) -> Dict[str, Any]:
        """Provide a summary of the swarm and its relationships."""
        return {
            "total_agents": self.total_agents,
            "featured_agents": self.as_list(),
            "relationship_model": [
                {"from": "Astra", "to": "Orion", "relationship": "coordination"},
                {"from": "Echo", "to": "Lyra", "relationship": "empathy_to_expression"},
                {"from": "Nova", "to": "Quill", "relationship": "research_to_insight"},
                {"from": "Sable", "to": "Kite", "relationship": "trust_and_review"},
            ],
        }


class AgentOrchestrator:
    """Select the best agent and model for a user prompt."""

    def __init__(self, model_router):
        self.model_router = model_router
        self.swarm = AgentSwarm(total_agents=1_000_000)

    def decide_agent(self, user_input: str) -> str:
        """Choose the best specialized agent based on the prompt content."""
        text = user_input.lower()

        if any(
            keyword in text
            for keyword in ["code", "bug", "fix", "refactor", "test", "build"]
        ):
            return "Orion"
        if any(
            keyword in text
            for keyword in [
                "research",
                "compare",
                "find",
                "latest",
                "market",
                "trend",
            ]
        ):
            return "Nova"
        if any(
            keyword in text
            for keyword in ["plan", "roadmap", "timeline", "strategy", "launch"]
        ):
            return "Kite"
        if any(
            keyword in text
            for keyword in ["review", "quality", "audit", "check", "risk"]
        ):
            return "Sable"
        if any(
            keyword in text
            for keyword in ["write", "story", "content", "message", "copy"]
        ):
            return "Lyra"
        if any(
            keyword in text
            for keyword in ["voice", "talk", "speak", "listen", "hello", "hi"]
        ):
            return "Echo"
        if any(
            keyword in text
            for keyword in ["data", "pattern", "insight", "analysis"]
        ):
            return "Quill"

        return "Astra"

    def build_response_plan(self, user_input: str) -> dict:
        """Construct the chosen agent and model plan for an input."""
        agent_name = self.decide_agent(user_input)
        model = self.model_router.route(agent_name)
        profile = self.swarm.profile_for(agent_name)
        return {
            "agent": agent_name,
            "role": profile.role if profile else "General",
            "model": model,
            "user_input": user_input,
            "swarm_summary": self.swarm.summary(),
            "personality": profile.to_dict() if profile else {},
        }

    def get_swarm_summary(self) -> dict:
        """Return the current swarm summary."""
        return self.swarm.summary()


__all__ = ["AgentOrchestrator", "AgentProfile", "AgentSwarm"]
