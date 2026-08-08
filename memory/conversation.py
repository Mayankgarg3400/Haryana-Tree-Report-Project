from langchain_core.messages import HumanMessage, AIMessage

chat_history = []


def add_user_message(text: str):
    chat_history.append(HumanMessage(content=text))


def add_ai_message(text: str):
    chat_history.append(AIMessage(content=text))


def get_chat_history():
    return chat_history


def clear_chat():
    chat_history.clear()