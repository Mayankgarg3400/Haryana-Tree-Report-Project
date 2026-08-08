from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"

# DOCUMENT_DIR = RAW_DIR / "documents"
DOCUMENT_DIR = RAW_DIR

REPORT_DIR = RAW_DIR / "reports"

PDF_PATH = REPORT_DIR / "Main_Data.pdf"

CHROMA_DB = BASE_DIR / "chroma_db"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "qwen2.5:3b"