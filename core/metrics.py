from core.config import CONFIG
import random


def evaluate_outcome(state):

    cfg = CONFIG["main"]["metrics"]

    execution = state.get("execution_result", {})

    status_key = cfg["keys"]["status"]
    success_value = cfg["values"]["success"]

    execution_success = execution.get(status_key) == success_value

    health_cfg = cfg["health"]
    success_bias = health_cfg["success_bias"]

    system_healthy = execution_success and random.random() < success_bias
    recurrence = not system_healthy

    weights = cfg["weights"]

    score = (
        weights["execution"] * int(execution_success) +
        weights["health"] * int(system_healthy) -
        weights["recurrence"] * int(recurrence)
    )

    state["metrics"] = {
        "execution_success": execution_success,
        "system_healthy": system_healthy,
        "recurrence": recurrence,
        "score": round(score, cfg["round"])
    }

    return state