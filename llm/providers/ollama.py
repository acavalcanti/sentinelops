import requests


def generate(prompt, config):

    url = config["services"]["ollama"]["url"]

    try:
        res = requests.post(
            f"{url}/api/generate",
            json={
                "model": config["llm"]["model"],
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )
        res.raise_for_status()
        return res.json()["response"]

    except requests.exceptions.ConnectionError:
        return config["analysis"]["fallback_text"]
    except requests.exceptions.Timeout:
        return config["analysis"]["fallback_text"]
    except (KeyError, ValueError):
        return config["analysis"]["fallback_text"]