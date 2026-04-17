import requests

def generate(prompt, config):

    url = config["main"]["services"]["ollama"]["url"]

    res = requests.post(f"{url}/api/generate", json={
        "model": config["main"]["llm"]["model"],
        "prompt": prompt,
        "stream": False
    })

    return res.json()["response"]