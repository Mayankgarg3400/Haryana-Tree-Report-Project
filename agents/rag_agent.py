# from langchain_ollama import ChatOllama
# from rag.retriever import retriever
# from config import LLM_MODEL
# from prompts import SYSTEM_PROMPT

# llm = ChatOllama(
#     model=LLM_MODEL,
#     temperature=0
# )

# def ask_rag(question):

#     docs = retriever.invoke(question)

#     context = "\n\n".join(doc.page_content for doc in docs)

#     prompt = f"""
# {SYSTEM_PROMPT}

# Context:

# {context}

# Question:

# {question}
# """

#     response = llm.invoke(prompt)
#     return response.content


# from pathlib import Path

# from langchain_ollama import ChatOllama

# from rag.retriever import retriever
# from config import LLM_MODEL
# from prompts import SYSTEM_PROMPT


# llm = ChatOllama(
#     model=LLM_MODEL,
#     temperature=0
# )


# def ask_rag(question):

#     docs = retriever.invoke(question)

#     if not docs:
#         return "I couldn't find any relevant information."

#     # Context
#     context = "\n\n".join(doc.page_content for doc in docs)

#     prompt = f"""
# {SYSTEM_PROMPT}

# Context:
# {context}

# Question:
# {question}
# """

#     response = llm.invoke(prompt)

#     # -------- Sources --------

#     sources = []

#     for doc in docs:

#         source = Path(doc.metadata.get("source", "Unknown")).name

#         page = doc.metadata.get("page")

#         if page is not None:
#             page = page + 1

#         sources.append(
#             f"• {source} (Page {page})"
#         )

#     # Remove duplicate sources

#     sources = list(dict.fromkeys(sources))

#     final_answer = (
#         response.content
#         + "\n\n"
#         + "📚 Sources\n"
#         + "\n".join(sources)
#     )

#     return final_answer

# from pathlib import Path

# from langchain_ollama import ChatOllama

# from rag.retriever import retriever
# from config import LLM_MODEL
# from prompts import SYSTEM_PROMPT

# from memory.conversation import (
#     add_ai_message,
#     add_user_message,
#     get_chat_history,
# )

# llm = ChatOllama(
#     model=LLM_MODEL,
#     temperature=0,
# )


# def ask_rag(question):

#     docs = retriever.invoke(question)

#     if not docs:
#         return "I couldn't find any relevant information."

#     context = "\n\n".join(doc.page_content for doc in docs)

#     history = ""

#     for msg in get_chat_history():
#         role = "User" if msg.type == "human" else "Assistant"
#         history += f"{role}: {msg.content}\n"

#     prompt = f"""
# {SYSTEM_PROMPT}

# Previous Conversation:

# {history}

# Context:

# {context}

# Question:

# {question}
# """

#     response = llm.invoke(prompt)

#     add_user_message(question)
#     add_ai_message(response.content)

#     # ---------- Sources ----------

#     source_map = {}

#     for doc in docs:

#         file_name = Path(doc.metadata.get("source", "Unknown")).name

#         page = doc.metadata.get("page")

#         if page is not None:
#             page += 1

#         if file_name not in source_map:
#             source_map[file_name] = []

#         if page is not None:
#             source_map[file_name].append(page)

#     citation = "\n📚 Sources\n"

#     for file_name, pages in source_map.items():

#         if pages:
#             pages = sorted(set(pages))
#             citation += f"• {file_name} (Pages: {', '.join(map(str, pages))})\n"
#         else:
#             citation += f"• {file_name}\n"

#     return response.content + citation

# from pathlib import Path

# from langchain_ollama import ChatOllama

# from rag.retriever import retriever
# from config import LLM_MODEL
# from prompts import SYSTEM_PROMPT

# from memory.conversation import (
#     add_ai_message,
#     add_user_message,
#     get_chat_history,
# )

# llm = ChatOllama(
#     model=LLM_MODEL,
#     temperature=0,
# )


# def ask_rag(question):

#     docs = retriever.invoke(question)

#     if not docs:
#         return "I couldn't find any relevant information."

#     # Context
#     context = "\n\n".join(doc.page_content for doc in docs)

#     # Previous Conversation
#     history = ""

#     for msg in get_chat_history():
        

#         role = "User" if msg.type == "human" else "Assistant"

#         history += f"{role}: {msg.content}\n"

#     prompt = f"""
# {SYSTEM_PROMPT}

# Previous Conversation:

# {history}

# Context:

# {context}

# Question:

# {question}
# """

#     response = llm.invoke(prompt)

#     add_user_message(question)
#     add_ai_message(response.content)

#     # ---------- Sources ----------

#     source_map = {}

#     for doc in docs:

#         file_name = Path(doc.metadata.get("source", "Unknown")).name

#         page = doc.metadata.get("page")

#         if page is not None:
#             page += 1

#         if file_name not in source_map:
#             source_map[file_name] = []

#         if page is not None:
#             source_map[file_name].append(page)

#     citation = "\n📚 Sources\n"

#     for file_name, pages in source_map.items():

#         if pages:
#             pages = sorted(set(pages))
#             citation += f"• {file_name} (Pages: {', '.join(map(str, pages))})\n"
#         else:
#             citation += f"• {file_name}\n"

#     return response.content + citation

from pathlib import Path

from langchain_ollama import ChatOllama

from rag.retriever import get_relevant_docs
from config import LLM_MODEL
from prompts import SYSTEM_PROMPT

from memory.conversation import (
    add_ai_message,
    add_user_message,
    get_chat_history,
)

llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0,
    num_predict=300,   # caps response length -> faster replies
    keep_alive="30m",  # keeps model loaded in memory between questions
)


def ask_rag(question):

    docs = get_relevant_docs(question)

    if not docs:
        return "I couldn't find this information in the available documents."

    context = "\n\n".join(doc.page_content for doc in docs)

    print("\n----- DEBUG: RETRIEVED CONTEXT -----")
    print(context)
    print("----- END DEBUG -----\n")

    # Only use the last 3 exchanges — keeps the prompt short and fast
    recent_history = get_chat_history()[-6:]

    history = ""
    for msg in recent_history:
        role = "User" if msg.type == "human" else "Assistant"
        history += f"{role}: {msg.content}\n"

    prompt = f"""
{SYSTEM_PROMPT}

Previous Conversation:

{history}

Context:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    add_user_message(question)
    add_ai_message(response.content)

    # ---------- Sources ----------

    source_map = {}

    for doc in docs:

        file_name = Path(doc.metadata.get("source", "Unknown")).name
        page = doc.metadata.get("page")

        if page is not None:
            page += 1

        if file_name not in source_map:
            source_map[file_name] = []

        if page is not None:
            source_map[file_name].append(page)

    citation = "\n📚 Sources\n"

    for file_name, pages in source_map.items():
        if pages:
            pages = sorted(set(pages))
            citation += f"• {file_name} (Pages: {', '.join(map(str, pages))})\n"
        else:
            citation += f"• {file_name}\n"

    return response.content + citation