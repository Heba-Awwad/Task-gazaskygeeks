import streamlit as st
import random
from datetime import datetime

# Page Configuration

st.set_page_config(
    page_title="Mock ChatGPT App",
    page_icon="💬",
    layout="centered"
)


# App Title

st.title("💬 Mock ChatGPT-like Chat App")
st.caption("Built with Streamlit only - No LLMs or APIs")


# Session State Initialization

if "messages" not in st.session_state:
    st.session_state.messages = []


def generate_mock_reply(user_message):
    """
    Generate local mock responses without using
    any external AI model or API.
    """

    message = user_message.lower()

    greetings = ["hello", "hi", "hey"]

    if any(word in message for word in greetings):
        return "Hello! How can I help you today?"

    elif "your name" in message:
        return "I am a mock assistant built using Streamlit."

    elif "time" in message:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    elif "date" in message:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."


    elif "python" in message:
        return "Python is a powerful and beginner-friendly programming language."

    elif "streamlit" in message:
        return "Streamlit is a Python framework used to build interactive web applications easily."

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        random_responses = [
            "Interesting question!",
            "Can you tell me more?",
            "I understand.",
            "That sounds great!",
            "This is a locally generated mock response.",
            "I am not using any AI API.",
            "Thanks for your message!"
        ]

        return random.choice(random_responses)

# Display Previous Messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat Input

user_prompt = st.chat_input("Type your message here...")

# When User Sends Message

if user_prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

# Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate local mock response
    assistant_reply = generate_mock_reply(user_prompt)

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_reply) 
