class AgentOrchestrator:
    def __init__(self, model_router):
        self.model_router = model_router

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
        return "default"

    def build_response_plan(self, user_input: str) -> dict:
        agent = self.decide_agent(user_input)
        model = self.model_router.route(agent)
        return {
            "agent": agent,
            "model": model,
            "user_input": user_input
        }
