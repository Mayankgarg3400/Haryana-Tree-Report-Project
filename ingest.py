# from config import PDF_PATH

# from rag.loader import load_pdf
# from rag.splitter import split_documents
# from rag.embeddings import get_embedding_model
# from rag.vector_store import create_vector_store

# print("Loading PDF...")

# documents = load_pdf(PDF_PATH)

# print("Splitting...")

# chunks = split_documents(documents)

# print("Loading Embedding Model...")

# embeddings = get_embedding_model()

# print("Creating ChromaDB...")

# vectorstore = create_vector_store(
#     chunks,
#     embeddings
# )

# print("Done")


from config import DOCUMENT_DIR

from rag.loader import load_all_documents
from rag.splitter import split_documents
from rag.embeddings import get_embedding_model
from rag.vector_store import create_vector_store


print("=" * 60)
print("🌿 VanMitra AI - Data Ingestion")
print("=" * 60)

# Load all documents
print("\n📄 Loading Documents...\n")
documents = load_all_documents(DOCUMENT_DIR)

# Split into chunks
print("\n✂️ Splitting Documents...\n")
chunks = split_documents(documents)

print(f"✅ Created {len(chunks)} Chunks")

# Load embedding model
print("\n🧠 Loading Embedding Model...\n")
embeddings = get_embedding_model()

# Create vector database
print("\n💾 Creating ChromaDB...\n")
vectorstore = create_vector_store(
    chunks=chunks,
    embeddings=embeddings
)

print("\n" + "=" * 60)
print("✅ Vector Database Created Successfully!")
print(f"📚 Total Documents : {len(documents)}")
print(f"🧩 Total Chunks    : {len(chunks)}")
print("=" * 60)