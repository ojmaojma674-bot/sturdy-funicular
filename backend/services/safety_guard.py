from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import time


@dataclass
class SafetySignal:
    name: str
    value: float
    threshold: float
    severity: str = "medium"

    def triggered(self) -> bool:
        return self.value >= self.threshold


class SafetyGuard:
    """Protects the runtime from degradation and crash loops by coordinating safe fallback logic."""

    def __init__(self, max_risk: float = 0.75, cooldown_seconds: float = 10.0):
        self.max_risk = max_risk
        self.cooldown_seconds = cooldown_seconds
        self.last_protection_time = 0.0
        self.event_log: List[Dict[str, Any]] = []

    def evaluate(self, signals: List[SafetySignal]) -> Dict[str, Any]:
        risk_score = 0.0
        triggered: List[str] = []

        for signal in signals:
            if signal.triggered():
                triggered.append(signal.name)
                multiplier = {"low": 0.2, "medium": 0.35, "high": 0.6, "critical": 0.9}.get(signal.severity, 0.3)
                risk_score += signal.value * multiplier

        risk_score = min(risk_score, 1.0)
        result = {
            "risk_score": round(risk_score, 3),
            "triggered_signals": triggered,
            "safe_mode": risk_score >= self.max_risk,
            "recommended_actions": [],
        }

        if result["safe_mode"]:
            result["recommended_actions"] = self.trigger_protection(context={"signals": triggered})
        else:
            result["recommended_actions"] = [
                "continue_with_monitoring",
                "do_not_start_new_risky_workflows",
                "watch_for_repeat_failures",
            ]

        return result

    def trigger_protection(self, context: Optional[Dict[str, Any]] = None) -> List[str]:
        now = time.monotonic()
        if now - self.last_protection_time < self.cooldown_seconds:
            return [
                "protection_already_active",
                "defer_new_risk_actions",
                "keep_only_essential_services_running",
            ]

        self.last_protection_time = now
        reason = context.get("signals", []) if context else []
        self.event_log.append(
            {
                "timestamp": time.time(),
                "event": "safe_mode_triggered",
                "reason": reason,
            }
        )

        return [
            "pause_non_essential_workflows",
            "freeze_risky_agent_actions",
            "save_last_known_good_state",
            "activate_monitoring_only_mode",
            "notify_vhotiex_aegis_and_rex",
            "route_to_recovery_path",
        ]

    def safe_response(self, user_message: str) -> Dict[str, Any]:
        return {
            "status": "safe_mode",
            "message": user_message,
            "response": "The system detected instability risk and switched to protected mode. It is pausing risky execution and preserving the last known good state before continuing safely.",
            "agent": "VHOTIEX",
            "protection_active": True,
        }


__all__ = ["SafetyGuard", "SafetySignal"]
