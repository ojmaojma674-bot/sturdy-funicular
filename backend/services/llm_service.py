"""LLM service integration for the VHOTIEX AI backend."""

from __future__ import annotations

import os
from typing import Optional

try:
    from openai import OpenAI
except Exception:  # pragma: no cover - optional dependency at runtime
    OpenAI = None


class LLMService:
    """Thin wrapper around an OpenAI-compatible chat completion API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")
        self.enabled = bool(self.api_key)
        self.client = None

        if self.enabled and OpenAI is not None:
            kwargs = {"api_key": self.api_key}
            if self.base_url:
                kwargs["base_url"] = self.base_url
            self.client = OpenAI(**kwargs)

    def _build_system_prompt(self, agent_name: str) -> str:
        return (
            f"You are {agent_name}, a helpful VHOTIEX AI assistant. "
            "Respond clearly, warmly, and concisely. Keep answers practical, "
            "professional, and easy to understand."
        )

    def generate_response(self, user_message: str, agent_name: str = "Astra") -> str:
        """Generate a response from the configured LLM provider if available."""
        if not self.enabled or self.client is None:
            return (
                f"{agent_name} is ready to help, but no OpenAI API key is configured. "
                "Set OPENAI_API_KEY in the backend environment to enable live LLM responses."
            )

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._build_system_prompt(agent_name)},
                    {"role": "user", "content": user_message},
                ],
                temperature=0.7,
                max_tokens=512,
            )
            content = completion.choices[0].message.content
            if content is None:
                return "I could not generate a model response right now."
            return content.strip()
        except Exception:  # pragma: no cover - safe fallback for missing network/credentials
            return (
                f"{agent_name} is online, but the model request failed. "
                "Check OPENAI_API_KEY and connectivity, then retry."
            )


__all__ = ["LLMService"]
