from langchain_ollama import OllamaEmbeddings

from config import EMBEDDING_MODEL


def get_embedding_model():

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )

    return embeddings