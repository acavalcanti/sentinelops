import re
from core.config import CONFIG


def extract_target(log, fallback):

    pattern = CONFIG["decision"]["target_pattern"]
    match = re.search(pattern, log)

    return match.group(0) if match else fallback


def decision_agent(state):

    candidates = state.get("rag_candidates", [])

    if not candidates:
        state["decision"] = {}
        state["action_spec"] = {}
        state["decision_confidence"] = 0.0
        return state

    best = max(candidates, key=lambda x: x["score"])

    fallback_target = CONFIG["decision"]["default_target"]

    decision = {
        "action": best["action"],
        "target": extract_target(state["log"], fallback_target),
        "namespace": CONFIG["decision"]["default_namespace"]
    }

    state["decision"] = decision
    state["action_spec"] = decision
    state["decision_confidence"] = best["score"]

    return state