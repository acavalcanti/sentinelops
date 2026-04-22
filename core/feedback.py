from core.config import CONFIG
from rag.embedding import embed
from qdrant_client import QdrantClient
import hashlib

cfg = CONFIG["services"]["qdrant"]

client = QdrantClient(
    host=cfg["host"],
    port=cfg["port"]
)


def feedback_writeback(state):

    score = state.get("metrics", {}).get("score", 0)

    threshold = CONFIG["feedback"]["min_score"]

    if score < threshold:
        return

    vector = embed(state["log"])

    payload = {
        "action": state.get("action_spec", {}).get("action"),
        "source": "feedback",
        "confidence": state.get("final_confidence")
    }

    client.upsert(
        collection_name=CONFIG["rag"]["retrieval"]["collection"],
        points=[{
            "id": hashlib.sha256(state["log"].encode()).hexdigest(),
            "vector": vector,
            "payload": payload
        }]
    )
