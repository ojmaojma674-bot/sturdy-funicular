from __future__ import annotations

from dataclasses import dataclass


def require_env(value: str | None, name: str) -> str:
    if value is None or not value.strip():
        raise ValueError(f"Missing required environment variable: {name}")
    return value


@dataclass
class AppSettings:
    app_name: str = "VHOTIEX-Neural-Core"
    app_env: str = "development"
    model_path: str = "./artifacts/vhotiex_model.pt"
    log_level: str = "INFO"
    api_host: str = "0.0.0.0"
    api_port: int = 8000


def get_settings() -> AppSettings:
    import os

    return AppSettings(
        app_name=os.getenv("APP_NAME", "VHOTIEX-Neural-Core"),
        app_env=os.getenv("APP_ENV", "development"),
        model_path=os.getenv("MODEL_PATH", "./artifacts/vhotiex_model.pt"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        api_host=os.getenv("API_HOST", "0.0.0.0"),
        api_port=int(os.getenv("API_PORT", "8000")),
    )
