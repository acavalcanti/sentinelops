from typing import TypedDict, List, Dict, Optional

class State(TypedDict, total=False):
    log: str

    # analysis
    structured_facts: str
    analysis_confidence: float

    # signature
    signatures: List[tuple]

    # rag
    rag_candidates: List[Dict]
    rag_confidence: float

    # decision
    action_spec: Dict
    decision_confidence: float

    # governance
    arbiter_decision: str
    policy_result: Dict

    # execution
    execution_result: Dict
    system_health: bool

    # learning
    learning_record: Dict

    # errors
    error: str

    # trace
    trace: Dict
