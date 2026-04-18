from agents.analysis import analysis_agent
from agents.signature import signature_agent
from agents.rag import rag_agent
from agents.decision import decision_agent
from core.arbiter import confidence_arbiter
from execution.router import execute
from core.metrics import evaluate_outcome
from core.history import save_incident
from core.config import CONFIG


def run_pipeline(state):

    state = analysis_agent(state)
    state = signature_agent(state)
    state = rag_agent(state)
    state = decision_agent(state)

    state = confidence_arbiter(state)

    if state["arbiter_decision"] == "halt":
        state["execution_result"] = {
            "status": "blocked"
        }

    if state["arbiter_decision"] == "halt":
        state["execution_result"] = {
            "status": "blocked"
    }
    else:
        state["execution_result"] = {
            "status": "skipped",
            "reason": "advisory_mode"
        }

    state = evaluate_outcome(state)

    save_incident(state)

    return state