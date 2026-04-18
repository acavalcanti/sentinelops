from orchestrator.graph import build_graph

graph = build_graph()

def run(log):
#    return graph.invoke({"log": log})
    return run_pipeline({"log": log})