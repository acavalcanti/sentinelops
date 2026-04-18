import yaml

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

CONFIG = load_yaml("config/config.yaml")

CONFIG["signatures"] = load_yaml("config/signatures.yaml")["signatures"]
CONFIG["tools"] = load_yaml("config/tools.yaml")["tools"]
CONFIG["kb"] = load_yaml("config/kb.yaml")["kb"]
CONFIG["health"] = load_yaml("config/health.yaml")["health"]