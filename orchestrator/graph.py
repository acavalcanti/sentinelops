from langgraph.graph import StateGraph

from agents.analysis import analysis_agent
from agents.signature import signature_agent
from agents.rag import rag_agent
from agents.decision import decision_agent
from core.state import State
from core.policy import policy_check
from core.arbiter import confidence_arbiter


def policy_agent(state):
    state["policy_result"] = policy_check(state.get("action_spec", {}))
    return state


def build_graph():

    graph = StateGraph(State)

    graph.add_node("analysis_node", analysis_agent)
    graph.add_node("signature_node", signature_agent)
    graph.add_node("rag_node", rag_agent)
    graph.add_node("decision_node", decision_agent)
    graph.add_node("policy_node", policy_agent)
    graph.add_node("arbiter_node", confidence_arbiter)

    graph.set_entry_point("analysis_node")

    graph.add_edge("analysis_node", "signature_node")
    graph.add_edge("signature_node", "rag_node")
    graph.add_edge("rag_node", "decision_node")
    graph.add_edge("decision_node", "policy_node")
    graph.add_edge("policy_node", "arbiter_node")

    graph.set_finish_point("arbiter_node")

    return graph.compile()