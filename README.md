# Task-gazaskygeeks
Chat
Technical Task - Build a ChatGPT-like App with Streamlit (No LLM)

Task:
Implement a ChatGPT-style chat application using Streamlit in Python, without using any external Large Language Model (LLM) or API.

The app uses Streamlit’s:

* st.chat_message
* st.chat_input

components to create a simple chat interface where users can type messages and receive mock assistant replies generated locally by a small Python function.

The conversation history is stored in:

* st.session_state.messages

so previous messages stay visible and the chat feels like a real conversation.

The whole application is contained in a single:

* chat_app.py

file that runs with:

streamlit run chat_app.py

The code is uploaded to a GitHub repository.

A short 2-minute YouTube video demonstrates:

* how the app runs
* how the user interacts with it
* clearly explains the code steps
* how the responses are simulated locally without any external LLM or API

highlighting skills in:

* Python
* Streamlit basics
* simple state management

IMPORTANT NOTE:
No external APIs or LLMs required.

Acceptance Criteria:

* No external LLMs or third-party APIs are used
* The application is built using Streamlit chat components
* Chat history is stored and displayed correctly during the session
* Mock response logic is implemented (no real AI integration required)
* The application runs successfully locally using Streamlit
