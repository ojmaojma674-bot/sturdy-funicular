from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentProfile:
    name: str
    type: str
    role: str
    primary_functions: List[str] = field(default_factory=list)
    backup_group: str = "core"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": self.type,
            "role": self.role,
            "primary_functions": self.primary_functions,
            "backup_group": self.backup_group,
        }


class AgentBackupCatalog:
    """Reference backup catalog for the VHOTIEX AI swarm."""

    def __init__(self) -> None:
        self.agents = [
            AgentProfile(
                name="VHOTIEX",
                type="commander",
                role="Coordinates all agents, gathers context, synthesizes final outputs, and decides escalation or action.",
                primary_functions=["orchestration", "final synthesis", "task routing", "decision making"],
                backup_group="core",
            ),
            AgentProfile(
                name="TITAN",
                type="compute",
                role="Handles heavy computational tasks, large-scale processing, and deep workload analysis.",
                primary_functions=["large computations", "data processing", "performance heavy tasks"],
                backup_group="core",
            ),
            AgentProfile(
                name="ECHO",
                type="voice",
                role="Processes speech recognition, voice commands, and conversational input streams.",
                primary_functions=["speech recognition", "voice commands", "audio understanding"],
                backup_group="core",
            ),
            AgentProfile(
                name="PULSE",
                type="monitoring",
                role="Tracks live state, system health, notifications, and critical events.",
                primary_functions=["real-time status", "monitoring", "notifications"],
                backup_group="core",
            ),
            AgentProfile(
                name="SPECTRA",
                type="experience",
                role="Designs UI/UX experiences, holographic visuals, and interface intelligence.",
                primary_functions=["ui design", "ux strategy", "holographic interfaces"],
                backup_group="core",
            ),
            AgentProfile(
                name="VECTOR",
                type="execution",
                role="Executes tasks, automates workflows, and manages operational action chains.",
                primary_functions=["task execution", "workflow orchestration", "automation"],
                backup_group="core",
            ),
            AgentProfile(
                name="REX",
                type="recovery",
                role="Runs validation, testing, error detection, and recovery flows.",
                primary_functions=["testing", "error recovery", "fault detection"],
                backup_group="core",
            ),
            AgentProfile(
                name="QUANTUM",
                type="reasoning",
                role="Performs advanced reasoning, strategic analysis, and multi-step planning.",
                primary_functions=["deep reasoning", "advanced analysis", "strategy"],
                backup_group="core",
            ),
            AgentProfile(
                name="PROMETHEUS",
                type="innovation",
                role="Builds new tools, prototypes, and experimental capabilities.",
                primary_functions=["prototype creation", "tool design", "innovation"],
                backup_group="core",
            ),
            AgentProfile(
                name="HELIOS",
                type="knowledge",
                role="Handles knowledge synthesis, system analytics, and information insight.",
                primary_functions=["knowledge retrieval", "analytics", "system intelligence"],
                backup_group="core",
            ),
            AgentProfile(
                name="FORGE",
                type="engineering",
                role="Handles coding, app development, debugging, and software construction workflows.",
                primary_functions=["software engineering", "debugging", "build management"],
                backup_group="specialist",
            ),
            AgentProfile(
                name="AEGIS",
                type="security",
                role="Performs security audits, permission checks, and vulnerability detection.",
                primary_functions=["security review", "permission checks", "vulnerability detection"],
                backup_group="specialist",
            ),
            AgentProfile(
                name="EVOLVE",
                type="optimization",
                role="Improves system performance, validates enhancements, and supports iterative optimization.",
                primary_functions=["self-improvement", "performance analysis", "validated improvements"],
                backup_group="specialist",
            ),
        ]

    def by_name(self, name: str) -> Optional[AgentProfile]:
        for agent in self.agents:
            if agent.name.lower() == name.lower():
                return agent
        return None

    def as_list(self) -> List[Dict[str, Any]]:
        return [agent.to_dict() for agent in self.agents]


__all__ = ["AgentProfile", "AgentBackupCatalog"]
