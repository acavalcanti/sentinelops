from llm.providers.ollama import generate
from core.config import CONFIG
import random


def analysis_agent(state):

    cfg = CONFIG["main"]["analysis"]

    print(CONFIG["main"]["analysis"])

    prompt_template = cfg["prompt"]
    prompt = prompt_template.format(log=state["log"])

    result = generate(prompt, CONFIG)

    fallback_text = cfg["fallback_text"]
    state["analysis"] = result if result else fallback_text

    conf_cfg = cfg["confidence"]

    base = conf_cfg["base"]
    variance_min = conf_cfg["variance_min"]
    variance_max = conf_cfg["variance_max"]
    max_val = conf_cfg["max"]
    precision = conf_cfg["precision"]

    confidence = base + random.uniform(variance_min, variance_max)

    state["analysis_confidence"] = round(
        min(confidence, max_val),
        precision
    )

    return state