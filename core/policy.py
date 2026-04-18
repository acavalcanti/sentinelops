from core.config import CONFIG

def policy_check(action_spec):

    cfg = CONFIG["policy"]

    if not cfg.get("enabled", True):
        return {"approved": True}

    if not action_spec:
        return {"approved": False, "reason": "no_action"}

    rules = cfg.get("rules", {})
    rule = rules.get(action_spec["action"])

    if not rule or not rule.get("allowed", False):
        return {"approved": False, "reason": "blocked"}

    return {
        "approved": True,
        "risk": rule.get("risk", cfg.get("default_risk"))
    }