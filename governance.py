
def policy_check(fix):
    return "blocked" if "delete" in fix else "allowed"

def risk_assessment(fix):
    return "high" if "delete" in fix else "medium"

def confidence_score(fix):
    return 0.75

def decision(policy, risk, confidence):
    if policy=="blocked":
        return "deny","Unsafe action blocked"
    if confidence<0.6 or risk=="high":
        return "human_review","Requires human approval"
    return "auto_execute","Safe to execute"
