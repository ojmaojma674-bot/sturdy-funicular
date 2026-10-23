"""Tool execution stub for mock system actions used by the backend."""


class ToolExecutor:
    """Dispatch a named tool to a simple placeholder implementation."""

    def __init__(self):
        self.tools = {
            "search": self._search_tool,
            "calculator": self._calculator_tool,
            "parser": self._parser_tool,
            "code_exec": self._code_exec_tool,
        }

    def _search_tool(self, query: str):
        """Return a mock search result for the provided query."""
        return {"tool": "search", "query": query, "result": "mock search result"}

    def _calculator_tool(self, expression: str):
        """Return a mock calculator result for the provided expression."""
        return {
            "tool": "calculator",
            "expression": expression,
            "result": "computed",
        }

    def _parser_tool(self, payload: str):
        """Return a mock parsed payload result."""
        return {"tool": "parser", "payload": payload, "result": "parsed"}

    def _code_exec_tool(self, code: str):
        """Return a mocked sandbox execution result."""
        return {
            "tool": "code_exec",
            "code": code,
            "result": "sandbox execution placeholder",
        }

    def run(self, tool_name: str, payload: str):
        """Execute a named tool with the provided payload."""
        if tool_name not in self.tools:
            raise ValueError(f"Unsupported tool: {tool_name}")
        return self.tools[tool_name](payload)
