class ModelRouter:
    def __init__(self):
        self.model_map = {
            "coding": "gpt-code",
            "research": "gpt-research",
            "analysis": "gpt-analysis",
            "planning": "gpt-planning",
            "review": "gpt-review",
            "voice": "gpt-voice",
            "default": "gpt-fast"
        }

    def route(self, agent_type: str) -> str:
        return self.model_map.get(agent_type, self.model_map["default"])
