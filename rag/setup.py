from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from rag.embedding import embed
from core.config import CONFIG


def ensure_collection():

    cfg = CONFIG["services"]["qdrant"]
    emb_cfg = CONFIG["embedding"]
    collection = CONFIG["rag"]["retrieval"]["collection"]

    client = QdrantClient(cfg["host"], port=cfg["port"])

    collections = client.get_collections().collections
    existing = [c.name for c in collections]

    if collection not in existing:

        client.create_collection(
            collection_name=collection,
            vectors_config=VectorParams(
                size=emb_cfg["dimension"],
                distance=Distance.COSINE
            ),
        )


        if client.count(collection_name=collection).count == 0:

            for i, item in enumerate(CONFIG["kb"]):

                client.upsert(
                    collection_name=collection,
                    points=[{
                        "id": i,
                        "vector": embed(item["signature"]),
                        "payload": {
                            "action": item["action"],
                            "signature": item["signature"]
                        }
                    }]
                )