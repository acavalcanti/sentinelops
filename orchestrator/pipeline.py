from orchestrator.graph import build_graph
from core.metrics import evaluate_outcome
from core.history import save_incident
from core.config import CONFIG
from core.observability import emit_trace
from core.feedback import feedback_writeback
from rag.setup import ensure_collection
from execution.router import execute 

def run_pipeline(state):

    graph = build_graph()

    ensure_collection()

    state = graph.invoke(state)

    decision = state.get("arbiter_decision", "halt")

    if decision == "halt":

        state["execution_result"] = {
            "status": CONFIG["execution"]["blocked_status"]
        }

    elif decision == "review":

        state["execution_result"] = {
            "status": CONFIG["execution"]["skipped_status"],
            "reason": "Requires human review",
            "action": state.get("action_spec")
        }

    else:  
        state["execution_result"] = execute(state.get("action_spec"))  

    state = evaluate_outcome(state)

    save_incident(state)

    score = state.get("metrics", {}).get("score", 0)

    if score >= CONFIG["feedback"]["min_score"]:
        feedback_writeback(state)

    trace = emit_trace(state)
    state["trace"] = trace

    return state