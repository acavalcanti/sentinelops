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
        limit=retrieval_cfg["top_k"] * 3 
    ).points

    norm_score = retrieval_cfg["norm_score"]

    if not results:
        state["rag_candidates"] = []
        state["rag_confidence"] = retrieval_cfg["default_confidence"]
        return state

    seen_actions = set()
    diverse_results = []

    for r in sorted(results, key=lambda x: x.score, reverse=True):
        action = r.payload.get("action")

        if action not in seen_actions:
            seen_actions.add(action)
            diverse_results.append(r)

        if len(diverse_results) >= retrieval_cfg["top_k"]:
            break

    candidates = []

    for r in diverse_results:

        base_score = r.score
        payload_conf = r.payload.get("confidence", 0)

        adjusted_score = (
            0.7 * base_score +
            0.3 * payload_conf
        )

        normalized_score = min(adjusted_score, norm_score)

        candidates.append({
            "action": r.payload.get("action"),
            "score": normalized_score
        })

    unique = {}

    for c in candidates:
        action = c["action"]
        if action not in unique or c["score"] > unique[action]["score"]:
            unique[action] = c

    candidates = list(unique.values())

    scores = [c["score"] for c in candidates]

    state["rag_candidates"] = candidates

    state["rag_confidence"] = (
        sum(scores) / len(scores)
        if scores else retrieval_cfg["default_confidence"]
    )

    return state