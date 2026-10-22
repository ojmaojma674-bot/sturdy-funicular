class MemoryService:
    def __init__(self):
        self.context = []

    def add_memory(self, user_input: str, response: str):
        self.context.append({
            "user_input": user_input,
            "response": response
        })

    def get_recent_context(self, limit: int = 5):
        return self.context[-limit:]
