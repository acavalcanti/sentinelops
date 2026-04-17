from core.config import CONFIG

def decision_agent(state):

    candidates = state["rag_candidates"]

    if not candidates:
        state["action_spec"] = None
        state["decision_confidence"] = CONFIG["main"]["agents"]["defaults"]["low_confidence"]
        return state

    best = candidates[0]

    state["action_spec"] = {
        "action": best["action"],
        "target": state.get("target", "default-service"),
        "namespace": state.get("namespace", "default"),
        "params": {}
    }

    state["decision_confidence"] = best["score"]

    return state