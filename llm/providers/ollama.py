import requests
import json


def generate(prompt, config):

    url = config["services"]["ollama"]["url"]

    res = requests.post(f"{url}/api/generate", json={
        "model": config["llm"]["model"],
        "prompt": prompt,
        "stream": False
    })

    return res.json()["response"]

def stream_generate(prompt, config):

    url = config["services"]["ollama"]["url"]

    response = requests.post(
        f"{url}/api/generate",
        json={
            "model": config["llm"]["model"],
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode())
            yield data.get("response", "")