"""Simple in-memory history tracking for chat interactions."""


class MemoryService:
    """Store recent chat context for short-lived conversational memory."""

    def __init__(self):
        self.context = []

    def add_memory(self, user_input: str, response: str):
        """Persist a user input and response pair in memory."""
        self.context.append({
            "user_input": user_input,
            "response": response,
        })

    def get_recent_context(self, limit: int = 5):
        """Return the most recent memory entries, capped by the limit."""
        return self.context[-limit:]
