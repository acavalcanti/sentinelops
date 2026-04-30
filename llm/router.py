from core.config import CONFIG
from llm.providers.ollama import generate


def call_llm(prompt):
    provider = CONFIG["llm"]["provider"]
    if provider == "openshift":
        from llm.providers.openshift import generate
    else:
        from llm.providers.ollama import generate
    return generate(prompt, CONFIG)