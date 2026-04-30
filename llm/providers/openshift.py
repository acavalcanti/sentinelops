import requests


def generate(prompt, config):

    url = config["services"]["llm"]["url"]
    api_key = config["services"]["llm"].get("api_key", "")
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    try:
        res = requests.post(
            url,
            json={"messages": [{"role": "user", "content": prompt}]},
            headers=headers,
            timeout=30
        )
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]

    except requests.exceptions.ConnectionError:
        return config["analysis"]["fallback_text"]
    except requests.exceptions.Timeout:
        return config["analysis"]["fallback_text"]
    except (KeyError, ValueError):
        return config["analysis"]["fallback_text"]