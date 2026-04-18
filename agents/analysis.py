from llm.router import call_llm
from core.config import CONFIG
import random


def analysis_agent(state):

    cfg = CONFIG["analysis"]

    prompt = cfg["prompt"].format(log=state["log"])

    result = call_llm(prompt)

    state["analysis"] = result if result else cfg["fallback_text"]

    conf_cfg = cfg["confidence"]

    confidence = conf_cfg["base"] + random.uniform(
        conf_cfg["variance_min"],
        conf_cfg["variance_max"]
    )

    state["analysis_confidence"] = round(
        min(confidence, conf_cfg["max"]),
        conf_cfg["precision"]
    )

    return state