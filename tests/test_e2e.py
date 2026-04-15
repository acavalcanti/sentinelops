
from orchestrator import orchestrator

def test_flow():
    r = orchestrator("ERROR: timeout")
    assert "timeline" in r
    assert "decision" in r
