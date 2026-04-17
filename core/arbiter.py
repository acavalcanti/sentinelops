from core.config import CONFIG

def confidence_arbiter(state):

    cfg = CONFIG["main"]["arbiter"]["thresholds"]

    scores = [
        state.get("analysis_confidence", 0),
        state.get("retrieval_confidence", 0),
        state.get("decision_confidence", 0)
    ]

    min_score = min(scores)

    if min_score < cfg["hard"]:
        state["arbiter_decision"] = "halt"
    elif min_score < cfg["soft"]:
        state["arbiter_decision"] = "escalate"
    else:
        state["arbiter_decision"] = "proceed"

    return state