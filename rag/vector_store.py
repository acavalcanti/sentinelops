
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

def build_index():
    with open("rag/runbooks.txt") as f:
        text = f.read()

    splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    docs = splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(docs, embeddings)
    db.save_local("rag/index")

def retrieve_context(query):
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("rag/index", embeddings)
    docs = db.similarity_search(query, k=2)
    return " ".join([d.page_content for d in docs])
