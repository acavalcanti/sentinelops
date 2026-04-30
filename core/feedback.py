from core.config import CONFIG
from rag.embedding import embed
from qdrant_client import QdrantClient
import uuid

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

    base_conf = state.get("final_confidence", 0)

    confidence = min(base_conf * 0.8, 0.85)

    payload = {
        "action": state.get("action_spec", {}).get("action"),
        "log": state.get("log"),
        "source": "feedback",
        "confidence": confidence
    }

    point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, state["log"]))

    client.upsert(
        collection_name=CONFIG["rag"]["retrieval"]["collection"],
        points=[{
            "id": point_id,
            "vector": vector,
            "payload": payload
        }]
    )

