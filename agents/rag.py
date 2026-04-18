from core.config import CONFIG
from rag.embedding import embed
from qdrant_client import QdrantClient

client = QdrantClient(
    host=CONFIG["main"]["services"]["qdrant"]["host"],
    port=CONFIG["main"]["services"]["qdrant"]["port"]
)


def rag_agent(state):

    query_vector = embed(state["log"])

    top_k = CONFIG["main"]["rag"]["retrieval"]["top_k"]

    # 🔥 FIX AQUI
    results = client.query_points(
        collection_name="incidents",
        query=query_vector,
        limit=top_k
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

    if scores:
        state["rag_confidence"] = max(scores)
    else:
        state["rag_confidence"] = CONFIG["main"]["rag"]["retrieval"]["default_confidence"]

    return state