from orchestrator.graph import build_graph
from core.metrics import evaluate_outcome
from core.history import save_incident
from core.config import CONFIG

graph = build_graph()


def run_pipeline(state):

    state = graph.invoke(state)

    # execution advisory
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

    return state