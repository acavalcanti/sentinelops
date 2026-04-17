from sentence_transformers import SentenceTransformer
from core.config import CONFIG

cfg = CONFIG["main"]["embedding"]

model = SentenceTransformer(cfg["model"])

def embed(text):
    return model.encode(text).tolist()