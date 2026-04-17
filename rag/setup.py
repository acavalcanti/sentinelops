from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from rag.embedding import embed
from core.config import CONFIG

def init_qdrant():

    cfg = CONFIG["main"]["services"]["qdrant"]
    emb_cfg = CONFIG["main"]["embedding"]

    client = QdrantClient(cfg["host"], port=cfg["port"])

    # recria coleção (reset)
    client.recreate_collection(
        collection_name="incidents",
        vectors_config=VectorParams(
            size=emb_cfg["dimension"],
            distance=Distance.COSINE
        ),
    )

    for i, item in enumerate(CONFIG["kb"]):

        client.upsert(
            collection_name="incidents",
            points=[{
                "id": i,
                "vector": embed(item["signature"]),
                "payload": {
                    "action": item["action"],
                    "signature": item["signature"]
                }
            }]
        )