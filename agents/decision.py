def decision_agent(state):

    candidates = state.get("rag_candidates", [])

    if not candidates:
        state["decision"] = {}
        state["action_spec"] = {}
        state["decision_confidence"] = 0.0
        return state

    best = max(candidates, key=lambda x: x["score"])

    action = best["action"]

    decision = {
        "action": action,
        "target": "order-service",
        "namespace": "default"
    }

    state["decision"] = decision
    state["action_spec"] = decision
    state["decision_confidence"] = best["score"]

    return state