import requests

def generate(prompt, config):

    url = config["main"]["services"]["llm"]["url"]

    res = requests.post(url, json={
        "messages": [{"role": "user", "content": prompt}]
    })

    return res.json()["choices"][0]["message"]["content"]