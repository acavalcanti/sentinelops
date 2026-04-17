from langgraph.graph import StateGraph

from agents.analysis import analysis_agent
from agents.signature import signature_agent
from agents.rag import rag_agent
from agents.decision import decision_agent

from core.arbiter import confidence_arbiter
from core.policy import policy_check
from execution.router import execute
from core.learning import compute_learning

def build_graph():

    graph = StateGraph(dict)

    graph.add_node("analysis", analysis_agent)
    graph.add_node("signature", signature_agent)
    graph.add_node("rag", rag_agent)
    graph.add_node("decision", decision_agent)
    graph.add_node("arbiter", confidence_arbiter)

    graph.add_edge("analysis", "signature")
    graph.add_edge("signature", "rag")
    graph.add_edge("rag", "decision")
    graph.add_edge("decision", "arbiter")

    graph.set_entry_point("analysis")

    return graph.compile()