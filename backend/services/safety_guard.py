"""Model routing helpers that map agent types to model names."""


class ModelRouter:
    """Route an agent or intent to a recommended model family."""

    def __init__(self):
        self.model_map = {
            "Astra": "gpt-orchestrator",
            "Nova": "gpt-research",
            "Lyra": "gpt-creative",
            "Orion": "gpt-code",
            "Echo": "gpt-conversation",
            "Sable": "gpt-review",
            "Kite": "gpt-planning",
            "Quill": "gpt-analysis",
            "coding": "gpt-code",
            "research": "gpt-research",
            "analysis": "gpt-analysis",
            "planning": "gpt-planning",
            "review": "gpt-review",
            "voice": "gpt-conversation",
            "default": "gpt-fast",
        }

    def route(self, agent_type: str) -> str:
        """Return the model for the given agent or intent name."""
        return self.model_map.get(agent_type, self.model_map["default"])
