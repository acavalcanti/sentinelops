from core.config import CONFIG

def compute_learning(state):

    weights = CONFIG["learning"]["weights"]

    success = state["execution_result"]["status"] == "success"
    health = state["system_health"]

    score = (
        weights["success"] * int(success) +
        weights["health"] * int(health)
    )

    state["learning_record"] = {"score": score}

    return state