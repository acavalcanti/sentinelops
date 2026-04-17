from core.config import CONFIG

def signature_agent(state):

    log = state["log"].lower()
    matches = []

    for sig in CONFIG["signatures"]:
        if any(term in log for term in sig["match"]):
            matches.append((sig["name"], sig["confidence"]))

    if not matches:
        defaults = CONFIG["main"]["agents"]["defaults"]
        matches = [(defaults["unknown_signature"], defaults["unknown_confidence"])]

    state["signatures"] = matches

    return state