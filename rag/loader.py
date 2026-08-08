# from langchain_community.document_loaders import PyPDFLoader

# def load_pdf(pdf_path):

#     loader = PyPDFLoader(str(pdf_path))

#     documents = loader.load()

#     print(f"Loaded {len(documents)} pages")

#     return documents

from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
)


def load_all_documents(data_dir: Path):
    """
    Load all PDFs and DOCX files from the data directory.
    """
    print(f"Searching inside: {data_dir}")

    documents = []

    # -------- PDFs --------
    pdf_files = list((data_dir / "reports").glob("*.pdf"))

    print(f"\nFound {len(pdf_files)} PDF files")

    for pdf in pdf_files:
        print(f"Loading PDF: {pdf.name}")

        loader = PyPDFLoader(str(pdf))
        docs = loader.load()

        print(f"   Loaded {len(docs)} pages")

        documents.extend(docs)

    # -------- DOCX --------
    docx_files = list((data_dir / "docs").glob("*.docx"))

    print(f"\nFound {len(docx_files)} DOCX files")

    for doc in docx_files:
        print(f"Loading DOCX: {doc.name}")

        loader = Docx2txtLoader(str(doc))
        docs = loader.load()

        print(f"   Loaded {len(docs)} document(s)")

        documents.extend(docs)

    print("\n===============================")
    print(f"Total Documents Loaded : {len(documents)}")
    print("===============================\n")

    return documents