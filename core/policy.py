from core.config import CONFIG

def policy_check(action_spec):

    if not CONFIG["main"]["policy"]["enabled"]:
        return {"approved": True}

    if not action_spec:
        return {"approved": False}

    return {
        "approved": True,
        "risk_score": CONFIG["main"]["policy"]["default_risk"]
    }