from rag.retriever import retriever

while True:

    question = input("\nQuestion : ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    print("\nRetrieved Documents\n")

    for i, doc in enumerate(docs, start=1):
        print("=" * 70)
        print(f"Chunk {i}")
        print(doc.page_content[:1200])
        print()