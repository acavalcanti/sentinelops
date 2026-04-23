from core.config import CONFIG


def confidence_arbiter(state):

    cfg = CONFIG["arbiter"]

    policy = state.get("policy_result", {})

    if not policy.get("approved", True):
        state["arbiter_decision"] = "halt"
        state["final_confidence"] = 0
        state["arbiter_reason"] = {
            "reason": "policy_denied",
            "policy": policy
        }
        return state

    weights = cfg["weights"]
    thresholds = cfg["thresholds"]
    precision = cfg["precision"]

    hard = thresholds["hard"]
    review = thresholds["review"]

    if hard > review:
        raise ValueError("Invalid arbiter thresholds: hard > review")

    analysis = state.get("analysis_confidence", 0.0)
    rag = state.get("rag_confidence", 0.0)
    decision = state.get("decision_confidence", 0.0)

    total_weight = sum(weights.values()) or 1

    final_conf = (
        analysis * weights["analysis"] +
        rag * weights["rag"] +
        decision * weights["decision"]
    ) / total_weight

    final_conf = round(final_conf, precision)

    state["final_confidence"] = final_conf

    if final_conf < hard:
        arbiter_decision = "halt"
    elif final_conf < review:
        arbiter_decision = "review"
    else:
        arbiter_decision = "proceed"

    state["arbiter_decision"] = arbiter_decision

    state["arbiter_reason"] = {
        "final_confidence": final_conf,
        "thresholds": thresholds,
        "inputs": {
            "analysis": analysis,
            "rag": rag,
            "decision": decision
        }
    }

    print("INPUTS:", analysis, rag, decision)
    print("WEIGHTS:", weights)
    print("FINAL:", final_conf)

    print("ARB INPUT:", {
        "analysis": analysis,
        "rag": rag,
        "decision": decision
    })

    return state