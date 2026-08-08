# def get_retriever(vectorstore):

#     retriever = vectorstore.as_retriever(
#         search_kwargs={"k":5}
#     )

#     return retriever

# from langchain_chroma import Chroma
# from langchain_ollama import OllamaEmbeddings
# from config import CHROMA_DB, EMBEDDING_MODEL

# embeddings = OllamaEmbeddings(
#     model=EMBEDDING_MODEL,
# )

# vectorstore = Chroma(
#     persist_directory=str(CHROMA_DB),
#     embedding_function=embeddings
# )

# retriever = vectorstore.as_retriever(
#     search_kwargs={"k": 5}
# )

# from langchain_chroma import Chroma
# from langchain_ollama import OllamaEmbeddings
# from config import CHROMA_DB, EMBEDDING_MODEL

# embeddings = OllamaEmbeddings(
#     model=EMBEDDING_MODEL,
# )

# vectorstore = Chroma(
#     persist_directory=str(CHROMA_DB),
#     embedding_function=embeddings
# )

# retriever = vectorstore.as_retriever(
#     search_type="mmr",#maximal marginal relevance
#     search_kwargs={
#         "k": 10,
#         "fetch_k": 20,
#         "lambda_mult": 0.7,
#     },
# )
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from config import CHROMA_DB, EMBEDDING_MODEL

embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL,
)

vectorstore = Chroma(
    persist_directory=str(CHROMA_DB),
    embedding_function=embeddings
)

# Fewer chunks + fewer fetch_k = much faster on a 3B model
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 6,
        "fetch_k": 15,
        "lambda_mult": 0.7,
    },
)

# All 22 Haryana districts — used to detect which district a question is about
HARYANA_DISTRICTS = [
    "Ambala", "Bhiwani", "Charkhi Dadri", "Faridabad", "Fatehabad",
    "Gurugram", "Gurgaon", "Hisar", "Jhajjar", "Jind", "Kaithal",
    "Karnal", "Kurukshetra", "Mahendragarh", "Nuh", "Palwal",
    "Panchkula", "Panipat", "Rewari", "Rohtak", "Sirsa",
    "Sonipat", "Yamunanagar", "Yamuna Nagar",
]


def extract_district(question: str):
    """Return the district name mentioned in the question, if any."""
    q_lower = question.lower()
    for district in HARYANA_DISTRICTS:
        if district.lower() in q_lower:
            return district
    return None


def get_relevant_docs(question: str):
    """
    Retrieve docs, then filter to the mentioned district if one is found.
    This fixes cross-district mix-ups (e.g. asking about Yamunanagar
    but getting an Ambala answer) without needing to re-ingest data.
    """
    docs = retriever.invoke(question)

    district = extract_district(question)

    if district:
        # Keep only chunks that actually mention this district
        filtered = [
            doc for doc in docs
            if district.lower() in doc.page_content.lower()
        ]
        # Only use the filtered set if it's not empty —
        # otherwise fall back to the original docs
        if filtered:
            docs = filtered

    # Cap context sent to the LLM — keeps responses fast
    return docs[:4]