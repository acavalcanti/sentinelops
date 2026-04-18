from langgraph.graph import StateGraph

from agents.analysis import analysis_agent
from agents.signature import signature_agent
from agents.rag import rag_agent
from agents.decision import decision_agent

from core.policy import policy_check
from core.arbiter import confidence_arbiter


def policy_agent(state):

    state["policy_result"] = policy_check(state.get("action_spec", {}))
    return state


def build_graph():

    graph = StateGraph(dict)

    graph.add_node("analysis", analysis_agent)
    graph.add_node("signature", signature_agent)
    graph.add_node("rag", rag_agent)
    graph.add_node("decision", decision_agent)
    graph.add_node("policy", policy_agent)
    graph.add_node("arbiter", confidence_arbiter)

    graph.set_entry_point("analysis")

    graph.add_edge("analysis", "signature")
    graph.add_edge("signature", "rag")
    graph.add_edge("rag", "decision")
    graph.add_edge("decision", "policy")
    graph.add_edge("policy", "arbiter")

    return graph.compile()