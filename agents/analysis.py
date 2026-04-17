from llm.router import call_llm
from core.config import CONFIG

def analysis_agent(state):

    prompt_template = CONFIG["main"]["analysis"].get(
        "prompt_template",
        "Analyze the following log:\n{log}"
    )

    prompt = prompt_template.format(log=state["log"])

    result = call_llm(prompt)

    state["structured_facts"] = result

    state["analysis_confidence"] = CONFIG["main"]["analysis"]["confidence"]["default"]

    return state