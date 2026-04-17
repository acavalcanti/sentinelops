import yaml

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

CONFIG = {
    "main": load_yaml("config/config.yaml"),
    "signatures": load_yaml("config/signatures.yaml")["signatures"],
    "tools": load_yaml("config/tools.yaml")["tools"],
    "kb": load_yaml("config/kb.yaml")["kb"],
    "health": load_yaml("config/health.yaml")["health"]
}