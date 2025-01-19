import streamlit as st
from ollama import chat

def get_response(messages, model='llama3.2:3b'):
    try:
        response = chat(model, messages=messages, stream=False)
        return response['message']['content']
    except Exception as e:
        st.error(f"Error: {e}")
        response = "Sorry, I couldn't process your request."
        return response



st.title("🦙 Llama Chat")

# Initialize the session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages in the session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a text input for the user
user_input = st.chat_input("Write your message here")

if user_input:
    # Display the user's message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get and display the assistant's response
    with st.chat_message("assistant"):
        messages = [{'role': 'user', 'content': user_input}]
        assistant_response = get_response(messages)
        st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})