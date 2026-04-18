from orchestrator.pipeline import run_pipeline


def run(log):
    return run_pipeline({"log": log})