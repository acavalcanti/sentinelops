from orchestrator.graph import build_graph
from core.metrics import evaluate_outcome
from core.history import save_incident
from core.config import CONFIG
from core.observability import emit_trace
from core.feedback import feedback_writeback

graph = build_graph()

def run_pipeline(state):

    state = graph.invoke(state)

    trace = emit_trace(state)
    state["trace"] = trace

    if state["arbiter_decision"] == "halt":
        state["execution_result"] = {
            "status": CONFIG["execution"]["blocked_status"]
        }
    else:
        state["execution_result"] = {
            "status": CONFIG["execution"]["skipped_status"],
            "reason": CONFIG["execution"]["advisory_reason"]
        }

    state = evaluate_outcome(state)

    save_incident(state)

    feedback_writeback(state)

    return state