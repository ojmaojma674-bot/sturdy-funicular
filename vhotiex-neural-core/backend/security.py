from __future__ import annotations

import re


def validate_feature_vector(features: list[float]) -> list[float]:
    if not isinstance(features, list):
        raise ValueError("Features must be provided as a list of numbers.")
    if len(features) != 128:
        raise ValueError("Exactly 128 features are required.")
    if any(not isinstance(value, (int, float)) for value in features):
        raise ValueError("All features must be numeric.")
    return features


def validate_intent_name(intent_name: str) -> str:
    if not isinstance(intent_name, str):
        raise ValueError("Intent name must be a string.")
    if not re.fullmatch(r"[a-z_\-]+", intent_name.lower()):
        raise ValueError("Intent name contains invalid characters.")
    return intent_name.lower()
