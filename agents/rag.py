from qdrant_client import QdrantClient
from rag.embedding import embed
from core.config import CONFIG

cfg = CONFIG["main"]["services"]["qdrant"]

client = QdrantClient(cfg["host"], port=cfg["port"])

def rag_agent(state):

    sig = state["signatures"][0][0]

    vector = embed(sig)

    rag_cfg = CONFIG["main"]["rag"]["retrieval"]

    results = client.search(
        collection_name="incidents",
        query_vector=vector,
        limit=rag_cfg["top_k"]
    )

    candidates = [
        {"action": r.payload["action"], "score": r.score}
        for r in results
    ]

    state["rag_candidates"] = candidates

    state["retrieval_confidence"] = (
        max([r.score for r in results], default=rag_cfg["default_confidence"])
    )

    return state