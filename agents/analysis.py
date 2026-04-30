from llm.router import call_llm
from core.config import CONFIG
import random


def analysis_agent(state):

    cfg = CONFIG["analysis"]
    conf_cfg = cfg["confidence"]

    prompt = cfg["prompt"].format(log=state["log"])

    result = call_llm(prompt)

    if not result or result == cfg["fallback_text"]:
        # LLM unavailable or returned nothing — use base confidence floor,
        # not random variance. A random score on zero-information analysis
        # would misrepresent the arbiter's input quality.
        state["analysis"] = cfg["fallback_text"]
        state["analysis_confidence"] = round(conf_cfg["base"], conf_cfg["precision"])
        return state

    state["analysis"] = result if result else cfg["fallback_text"]



    confidence = conf_cfg["base"] + random.uniform(
        conf_cfg["variance_min"],
        conf_cfg["variance_max"]
    )

    state["analysis_confidence"] = round(
        min(confidence, conf_cfg["max"]),
        conf_cfg["precision"]
    )

    return state