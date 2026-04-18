from core.config import CONFIG


def confidence_arbiter(state):

    cfg = CONFIG["arbiter"]

    weights = cfg["weights"]
    thresholds = cfg["thresholds"]

    final_conf = (
        state.get("analysis_confidence", 0.0) * weights["analysis"] +
        state.get("rag_confidence", 0.0) * weights["rag"] +
        state.get("decision_confidence", 0.0) * weights["decision"]
    )

    precision = cfg["precision"]

    state["final_confidence"] = round(final_conf, precision)

    if final_conf < thresholds["hard"]:
        decision = "halt"
    elif final_conf < thresholds["review"]:
        decision = "review"
    else:
        decision = "proceed"

    state["arbiter_decision"] = decision

    state["arbiter_reason"] = (
        f"confidence={round(final_conf, precision)} "
        f"thresholds={thresholds}"
    )

    return state