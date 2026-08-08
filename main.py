from agents.rag_agent import ask_rag

print("=" * 60)
print("🌿 VanMitra AI - Agentic Tree Plantation Assistant")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    q = input("\n🌱 Ask: ")

    if q.lower() in ["exit", "quit"]:
        print("\n👋 Thank you for using VanMitra AI!")
        break

    print("\n🤖 Thinking...\n")

    answer = ask_rag(q)

    print(answer)