import streamlit as st
from agents.rag_agent import ask_rag
from memory.conversation import clear_chat

# ---------------- Page Config ----------------

st.set_page_config(
    page_title="VanMitra AI",
    page_icon="🌿",
    layout="wide",
)

# ---------------- Session State ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ----------------

with st.sidebar:

    st.title("🌿 VanMitra AI")

    st.markdown("---")

    st.subheader("📂 Loaded Documents")

    st.success("Main_Data.pdf")
    st.success("Haryanaclimate.pdf")
    st.success("Soil Quality.pdf")
    st.success("Forest Contact No..pdf")
    st.success("Types of Trees.docx")
    st.success("Haryana General Data.docx")
    st.success("Report Conclusion.docx")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        clear_chat()
        st.rerun()

# ---------------- Header ----------------

st.title("🌿 VanMitra AI")

st.caption("Agentic Tree Plantation Assistant for Haryana Forest Department")

st.divider()

# ---------------- Previous Chat ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- Chat Input ----------------

question = st.chat_input("Ask anything about trees, climate, soil or forests...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("🌱 Thinking..."):

            answer = ask_rag(question)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )