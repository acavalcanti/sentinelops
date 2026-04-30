from core.config import CONFIG


def execute(action_spec, config=CONFIG):
    """
    Advisory-mode execution boundary (see ADR-002).

    This function is the intentional firewall between AI reasoning and real
    operational action. In production, this would dispatch to kubectl, Ansible,
    or an MCP tool registry based on action_spec.action.

    It is deliberately disconnected from real tooling so that:
    - The demo cannot cause unintended infrastructure changes
    - The boundary between 'decided' and 'executed' is architecturally explicit
    - A future production system can replace this single function

    Returns a structured advisory result. No real action is performed.
    """

    if not action_spec:
        return {
            "status": "skipped",
            "reason": "no action_spec"
        }

    return {
        "status": "advisory",
        "action": action_spec.get("action"),
        "target": action_spec.get("target"),
        "note": config["router"]["advisory"]["error"]
    }