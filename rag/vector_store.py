from langchain_chroma import Chroma

from config import CHROMA_DB


def create_vector_store(chunks, embeddings):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DB)
    )

    print("Vector Database Created")

    return vectorstore