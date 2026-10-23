"""Simple model routing for the VHOTIEX AI backend."""

from __future__ import annotations


class ModelRouter:
    """Map an agent name to a model selection."""

    _model_map = {
        "Astra": "gpt-4o-mini",
        "Nova": "gpt-4o-mini",
        "Lyra": "gpt-4o-mini",
        "Orion": "gpt-4o-mini",
        "Echo": "gpt-4o-mini",
        "Sable": "gpt-4o-mini",
        "Kite": "gpt-4o-mini",
        "Quill": "gpt-4o-mini",
    }

    def route(self, agent_name: str) -> str:
        """Return the default model for the named agent."""
        return self._model_map.get(agent_name, "gpt-4o-mini")

    def available_models(self) -> list[str]:
        """Return the currently supported model names."""
        return sorted(set(self._model_map.values()))
