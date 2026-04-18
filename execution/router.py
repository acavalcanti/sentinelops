from core.config import CONFIG


def execute(action_spec, config=CONFIG):

    if not action_spec:
        return {
            "status": "skipped",
            "reason": "no action_spec"
        }

    # MOCK EXECUTION
    return {
        "status": "success",
        "action": action_spec.get("action"),
        "target": action_spec.get("target")
    }