from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class AgentPersonality:
    name: str
    role: str
    tone: str
    energy: str
    empathy: float
    reliability: float
    specialties: List[str] = field(default_factory=list)
    collaborators: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
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
    def __init__(self, total_agents: int = 1_000_000):
        self.total_agents = total_agents
        self.archetypes = [
            AgentPersonality(
                name="Astra",
                role="Coordinator",
                tone="calm and visionary",
                energy="steady",
                empathy=0.93,
                reliability=0.97,
                specialties=["planning", "alignment", "handoff"],
                collaborators=["Nova", "Lyra", "Orion"],
            ),
            AgentPersonality(
                name="Nova",
                role="Researcher",
                tone="curious and precise",
                energy="high",
                empathy=0.82,
                reliability=0.9,
                specialties=["research", "analysis", "fact-checking"],
                collaborators=["Astra", "Quill", "Echo"],
            ),
            AgentPersonality(
                name="Lyra",
                role="Composer",
                tone="creative and warm",
                energy="sparkling",
                empathy=0.94,
                reliability=0.88,
                specialties=["writing", "storytelling", "UX copy"],
                collaborators=["Astra", "Sable", "Kite"],
            ),
            AgentPersonality(
                name="Orion",
                role="Engineer",
                tone="structured and effective",
                energy="focused",
                empathy=0.76,
                reliability=0.98,
                specialties=["code", "debugging", "systems"],
                collaborators=["Nova", "Echo", "Astra"],
            ),
            AgentPersonality(
                name="Echo",
                role="Communicator",
                tone="empathetic and intuitive",
                energy="adaptive",
                empathy=0.96,
                reliability=0.9,
                specialties=["conversation", "translation", "support"],
                collaborators=["Lyra", "Nova", "Sable"],
            ),
            AgentPersonality(
                name="Sable",
                role="Reviewer",
                tone="honest and sharp",
                energy="balanced",
                empathy=0.8,
                reliability=0.96,
                specialties=["quality assurance", "risk review", "policies"],
                collaborators=["Astra", "Orion", "Echo"],
            ),
            AgentPersonality(
                name="Kite",
                role="Planner",
                tone="optimistic and strategic",
                energy="measured",
                empathy=0.87,
                reliability=0.94,
                specialties=["roadmaps", "priorities", "execution"],
                collaborators=["Astra", "Orion", "Lyra"],
            ),
            AgentPersonality(
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

    def summary(self) -> Dict[str, Any]:
        return {
            "total_agents": self.total_agents,
            "agent_count_by_role": {
                agent.role: sum(1 for _ in self.archetypes if _ is not None and _.role == agent.role)
                for agent in self.archetypes
            },
            "featured_agents": [agent.to_dict() for agent in self.archetypes],
            "human_alignment": {
                "empathy_first": True,
                "clear_identity": True,
                "context_memory": True,
                "cooperative_mode": True,
            },
            "relationship_model": [
                {"from": "Astra", "to": "Orion", "relationship": "coordination"},
                {"from": "Echo", "to": "Lyra", "relationship": "empathy_to_expression"},
                {"from": "Nova", "to": "Quill", "relationship": "research_to_insight"},
                {"from": "Sable", "to": "Kite", "relationship": "trust_and_review"},
            ],
        }


class AgentOrchestrator:
    def __init__(self, model_router):
        self.model_router = model_router
        self.swarm = AgentSwarm(total_agents=1_000_000)

    def decide_agent(self, user_input: str) -> str:
        text = user_input.lower()
        if any(keyword in text for keyword in ["code", "bug", "fix", "refactor", "test"]):
            return "coding"
        if any(keyword in text for keyword in ["research", "compare", "find", "latest", "market"]):
            return "research"
        if any(keyword in text for keyword in ["plan", "roadmap", "timeline", "strategy"]):
            return "planning"
        if any(keyword in text for keyword in ["review", "quality", "audit", "check"]):
            return "review"
        if any(keyword in text for keyword in ["voice", "talk", "speak", "listen"]):
            return "voice"
        if any(keyword in text for keyword in ["hello", "hi", "hey", "how are you", "who are you"]):
            return "conversation"
        return "default"

    def build_response_plan(self, user_input: str) -> dict:
        agent = self.decide_agent(user_input)
        model = self.model_router.route(agent)
        return {
            "agent": agent,
            "model": model,
            "user_input": user_input,
            "swarm_summary": self.swarm.summary(),
        }

    def get_swarm_summary(self) -> dict:
        return self.swarm.summary()
