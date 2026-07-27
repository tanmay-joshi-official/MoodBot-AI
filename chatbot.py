import streamlit as st
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

load_dotenv()

# Page Config
st.set_page_config(
    page_title="Funny AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Funny AI Chatbot")
st.caption("Powered by LangChain + Mistral")

# Load Model
@st.cache_resource
def load_model():
    return init_chat_model(
        model="mistral-small-2506",
        temperature=0.9
    )

model = load_model()

# Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny AI agent.")
    ]

# Display Chat
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# User Input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

            st.markdown(response.content)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )