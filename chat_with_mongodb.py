from pymongo import MongoClient
import uuid
from datetime import datetime
import streamlit as st
from ollama import chat

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.chat_db

def add_message(chat_id, role, content):
    """Add a message to the chat-specific collection in the database."""
    collection = db[chat_id]
    collection.insert_one({"role": role, "content": content})

def get_all_messages(chat_id):
    """Fetch all messages for a specific chat_id from the chat-specific collection."""
    collection = db[chat_id]
    return list(collection.find({}, {"_id": 0, "role": 1, "content": 1}))

def create_new_chat():
    """Create a new chat instance, return its UUID, and create a new collection for it."""
    chat_id = str(uuid.uuid4())
    db.create_collection(chat_id)
    db.chat_metadata.insert_one({"chat_id": chat_id, "created_at": datetime.utcnow()})
    return chat_id

def get_all_chat_ids():
    """Fetch all unique chat IDs (collection names) from the database, sorted by creation time."""
    chat_ids = db.chat_metadata.find({}, {"_id": 0, "chat_id": 1, "created_at": 1}).sort("created_at", -1)
    return [f"{doc['chat_id'][:4]} ({doc['created_at'].strftime('%Y-%m-%d %H:%M:%S')})" for doc in chat_ids]


def get_response(messages, model='llama3.2:3b'):
    try:
        response = chat(model, messages=messages, stream=False)
        return response['message']['content']
    except Exception as e:
        st.error(f"Error: {e}")
        response = "Sorry, I couldn't process your request."
        return response

def get_streaming_response(messages, model='llama3.2:3b'):
    for part in chat(model, messages=messages, stream=True):
        yield part['message']['content']

st.title("🦙 Lamma Chat")

# Sidebar to display previous chats
st.sidebar.title("Previous Chats")
chat_ids = get_all_chat_ids()
selected_chat_id = st.sidebar.selectbox("Select a chat", chat_ids)

if selected_chat_id:
    st.session_state.chat_id = selected_chat_id.split()[0]  # Extract the UUID part

# Button to create a new chat
if st.sidebar.button("New Chat"):
    st.session_state.chat_id = create_new_chat()
    st.rerun()  # Reload the page to reflect the new chat

# Ensure chat_id is set in session state
if "chat_id" not in st.session_state:
    st.session_state.chat_id = create_new_chat()
    st.rerun()  # Reload the page to reflect the new chat

chat_id = st.session_state.chat_id

# Fetch all messages for the current chat_id from the database
messages = get_all_messages(chat_id)

# Display all messages from the database
for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a text input for the user
prompt = st.chat_input("Write your message here")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        add_message(chat_id, "user", prompt)

    # Include the new user message in the messages list
    messages.append({'role': 'user', 'content': prompt})
    response_content = ""

    with st.chat_message("assistant"):
        response = st.write_stream(get_streaming_response(messages))
        for part in response:
            response_content += part
            # st.markdown(part)

    add_message(chat_id, "assistant", response_content)
    messages.append({'role': 'assistant', 'content': response_content})

    