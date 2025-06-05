import faiss
import numpy as np
from embedding_utils import get_openai_embedding
from .external_data import fetch_city_documents
from .external_data import fetch_city_documents

def build_faiss_index(docs):
    texts = [doc["content"] for doc in docs]
    embeddings = get_openai_embedding(texts)
    arr = np.array(embeddings, dtype='float32')
    index = faiss.IndexFlatL2(arr.shape[1])
    index.add(arr)
    return index, texts

def retrieve_relevant_text(query, city, top_k=1):
    """
    Fetches city documents via API, builds FAISS index, and retrieves most relevant content.
    """
    documents = fetch_city_documents(city)
    if not documents:
        return ["No context data found."]
    faiss_index, texts = build_faiss_index(documents)
    q_emb = get_openai_embedding(query)[0]
    D, I = faiss_index.search(np.array([q_emb], dtype='float32'), top_k)
    results = [texts[i] for i in I[0]]
    return results


def retrieve_relevant_text(query, city, top_k=1, source="wikipedia"):
    """
    Fetches city documents via selected API, builds FAISS index, and retrieves relevant content.
    """
    documents = fetch_city_documents(city, source=source)
    if not documents:
        return ["No context data found."]
    faiss_index, texts = build_faiss_index(documents)
    q_emb = get_openai_embedding(query)[0]
    D, I = faiss_index.search(np.array([q_emb], dtype='float32'), top_k)
    results = [texts[i] for i in I[0]]
    return results
