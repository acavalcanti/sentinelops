from core.config import CONFIG
from llm.providers import ollama, openshift

def call_llm(prompt):

    provider = CONFIG["main"]["llm"]["provider"]

    if provider == "ollama":
        return ollama.generate(prompt, CONFIG)

    if provider == "openshift":
        return openshift.generate(prompt, CONFIG)