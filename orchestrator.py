
from planner import planner
from agents import analysis_agent, diagnosis_agent, fix_agent
from governance import policy_check, risk_assessment, confidence_score, decision
from itsm import create_ticket
from timeline import create_timeline, add_step

def orchestrator(log):
    timeline=create_timeline()
    plan=planner(log)
    add_step(timeline,"planner",str(plan))

    result={"plan":plan}

    if "analysis" in plan:
        result["analysis"]=analysis_agent(log)
        add_step(timeline,"analysis",result["analysis"])

    if "diagnosis" in plan:
        result["diagnosis"]=diagnosis_agent(log)
        add_step(timeline,"diagnosis",result["diagnosis"])

    if "fix" in plan:
        result["fix"]=fix_agent(result.get("diagnosis",result["analysis"]))
        add_step(timeline,"fix",result["fix"])

    policy=policy_check(result.get("fix",""))
    risk=risk_assessment(result.get("fix",""))
    confidence=confidence_score(result.get("fix",""))

    decision_result,explanation=decision(policy,risk,confidence)

    execution="success" if confidence>0.6 else "failure"
    add_step(timeline,"execution",execution)

    ticket=create_ticket(result.get("analysis"))

    result.update({
        "policy":policy,
        "risk":risk,
        "confidence":confidence,
        "decision":decision_result,
        "explanation":explanation,
        "execution":execution,
        "ticket":ticket,
        "timeline":timeline
    })
    return result
