import json
from datetime import datetime
from pathlib import Path
from core.config import CONFIG

cfg = CONFIG["history"]

HISTORY_FILE = Path(cfg["file"])
LIMIT = cfg["limit"]


def save_incident(state):

    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append({
        "timestamp": str(datetime.now()),
        "log": state.get("log"),
        "decision": state.get("decision"),
        "confidence": state.get("final_confidence"),
        "arbiter": state.get("arbiter_decision"),
        "metrics": state.get("metrics") or {}
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history[-LIMIT:], f, indent=2)