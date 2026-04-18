from core.config import CONFIG


def confidence_arbiter(state: dict) -> dict:

    cfg = CONFIG["main"]["arbiter"]

    thresholds = cfg["thresholds"]
    weights = cfg["weights"]

    hard = thresholds["hard"]
    review = thresholds["review"]
    soft = thresholds["soft"]

    w_analysis = weights["analysis"]
    w_rag = weights["rag"]
    w_decision = weights["decision"]

    analysis_conf = state.get("analysis_confidence", 0.0)
    rag_conf = state.get("rag_confidence", 0.0)
    decision_conf = state.get("decision_confidence", 0.0)

    final_conf = (
        analysis_conf * w_analysis +
        rag_conf * w_rag +
        decision_conf * w_decision
    )

    state["final_confidence"] = round(final_conf, 3)

    if final_conf < hard:
        state["arbiter_decision"] = "halt"

    elif final_conf < review:
        state["arbiter_decision"] = "review"

    else:
        state["arbiter_decision"] = "proceed"

    return state