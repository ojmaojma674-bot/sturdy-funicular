class ToolExecutor:
    def __init__(self):
        self.tools = {
            "search": self._search_tool,
            "calculator": self._calculator_tool,
            "parser": self._parser_tool,
            "code_exec": self._code_exec_tool,
        }

    def _search_tool(self, query: str):
        return {"tool": "search", "query": query, "result": "mock search result"}

    def _calculator_tool(self, expression: str):
        return {"tool": "calculator", "expression": expression, "result": "computed"}

    def _parser_tool(self, payload: str):
        return {"tool": "parser", "payload": payload, "result": "parsed"}

    def _code_exec_tool(self, code: str):
        return {"tool": "code_exec", "code": code, "result": "sandbox execution placeholder"}

    def run(self, tool_name: str, payload: str):
        if tool_name not in self.tools:
            raise ValueError(f"Unsupported tool: {tool_name}")
        return self.tools[tool_name](payload)
