import json
import datetime
from core.config import CONFIG


def build_trace(state):

    return {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "log": state.get("log"),
        "analysis_confidence": state.get("analysis_confidence"),
        "rag_confidence": state.get("rag_confidence"),
        "decision": state.get("decision"),
        "final_confidence": state.get("final_confidence"),
        "arbiter_decision": state.get("arbiter_decision"),
        "execution_result": state.get("execution_result")
    }


def emit_trace(state):

    trace = build_trace(state)

    print(json.dumps(trace, indent=2))

    return trace