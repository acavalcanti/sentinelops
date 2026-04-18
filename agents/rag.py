from core.config import CONFIG
from rag.embedding import embed
from qdrant_client import QdrantClient

cfg = CONFIG["services"]["qdrant"]

client = QdrantClient(
    host=cfg["host"],
    port=cfg["port"]
)


def rag_agent(state):

    query_vector = embed(state["log"])

    retrieval_cfg = CONFIG["rag"]["retrieval"]

    results = client.query_points(
        collection_name=retrieval_cfg["collection"],
        query=query_vector,
        limit=retrieval_cfg["top_k"]
    ).points

    candidates = []
    scores = []

    for r in results:
        candidates.append({
            "action": r.payload.get("action"),
            "score": r.score
        })
        scores.append(r.score)

    state["rag_candidates"] = candidates

    state["rag_confidence"] = (
        max(scores) if scores else retrieval_cfg["default_confidence"]
    )

    return state