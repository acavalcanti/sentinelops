import json
import datetime
from datetime import datetime, timezone
from core.config import CONFIG


def build_trace(state):

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "log": state.get("log"),
        "analysis_confidence": state.get("analysis_confidence"),
        "rag_confidence": state.get("rag_confidence"),
        "decision": state.get("action_spec"),
        "final_confidence": state.get("final_confidence"),
        "arbiter_decision": state.get("arbiter_decision"),
        "execution_result": state.get("execution_result"),
        "policy_result": state.get("policy_result"),
        "metrics": state.get("metrics"),
    }


def emit_trace(state):

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "log": state.get("log"),

        "analysis_confidence": state.get("analysis_confidence"),
        "rag_confidence": state.get("rag_confidence"),

        "decision": state.get("action_spec"),

        "decision_confidence": state.get("decision_confidence"),

        "final_confidence": state.get("final_confidence", 0),

        "arbiter_decision": state.get("arbiter_decision"),

        "execution_result": state.get("execution_result"),
        "policy_result": state.get("policy_result"),
        "metrics": state.get("metrics"),
    }