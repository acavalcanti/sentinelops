from core.config import CONFIG
from llm.providers.ollama import generate


def call_llm(prompt):
    return generate(prompt, CONFIG)