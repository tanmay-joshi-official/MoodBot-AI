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
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.caption("Just choose your AI mood and have a chat!")

# Mood Selection
mood_option = st.selectbox(
    "🎭 Choose AI Mood",
    (
        "Funny 😂",
        "Angry 😡",
        "Sad 😢",
    )
)

if mood_option == "Funny 😂":
    mood = "You are a Funny AI agent. You respond with humor and jokes."

elif mood_option == "Angry 😡":
    mood = "You are an Angry AI agent. You respond aggressively and impatiently."

elif mood_option == "Sad 😢":
    mood = "You are a Sad AI agent. You respond in a sad and sorrowful manner."

# Load Model
@st.cache_resource
def load_model():
    return init_chat_model(
        model="mistral-small-2506",
        temperature=0.9
    )

model = load_model()

# Reset Chat if Mood Changes
if (
    "current_mood" not in st.session_state
    or st.session_state.current_mood != mood
):
    st.session_state.current_mood = mood
    st.session_state.messages = [
        SystemMessage(content=mood)
    ]

# Display Messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Chat Input
prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

            st.markdown(response.content)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

# Clear Chat Button
st.divider()

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        SystemMessage(content=mood)
    ]
    st.rerun()