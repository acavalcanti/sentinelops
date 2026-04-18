from sentence_transformers import SentenceTransformer
from core.config import CONFIG

cfg = CONFIG["embedding"]

model = SentenceTransformer(cfg["model"])

def embed(text):
    return model.encode(text).tolist()