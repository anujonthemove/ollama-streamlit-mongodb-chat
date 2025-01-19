# ChatGPT-Like App with Streamlit, MongoDB, and Local LLMs

This repository contains the code for a ChatGPT-like application built using Streamlit for the user interface, MongoDB for persistent storage, and Ollama's local LLMs for generating AI responses. The application supports features like streaming responses, session state management, and persistent conversation history.

## Table of Contents

- [Features](#features)
- [File Overview](#file-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running MongoDB with Docker](#running-mongodb-with-docker)
- [Running the Application](#running-the-application)
- [How to Use the Application](#how-to-use-the-application)
- [Troubleshooting](#troubleshooting)

## Features

- Real-time chat interface using Streamlit.
- Persistent storage of conversations with MongoDB.
- Ability to retrieve and continue previous chat sessions.
- Streaming responses powered by local LLMs from Ollama.
- Organized and modular codebase with three levels of implementation:
  - Basic chat functionality (`simple_chat.py`).
  - Session state management (`chat_with_session_state.py`).
  - MongoDB integration (`chat_with_mongodb.py`).

## File Overview

- **`simple_chat.py`**: A basic implementation of the chat interface with minimal functionality.
- **`chat_with_session_state.py`**: Extends the basic app with session state for managing chat history during a session.
- **`chat_with_mongodb.py`**: Adds MongoDB integration to store and retrieve chat sessions and messages persistently.
- **`docker-compose.yml`**: Configuration for running MongoDB in a Docker container.

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or later
- Docker and Docker Compose
- Pip (Python package manager)
- [Ollama](https://ollama.ai) installed locally to access their models

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Make sure the `requirements.txt` file includes:
   - `streamlit`
   - `pymongo`
   - `ollama`

## Running MongoDB with Docker

1. **Start MongoDB**:
   Ensure Docker is running on your system, then run:
   ```bash
   docker-compose up -d
   ```

2. **Verify MongoDB is running**:
   Check the logs to confirm:
   ```bash
   docker-compose logs
   ```

   By default, MongoDB will be accessible at `mongodb://localhost:27017/`.

## Running the Application

1. **Choose a script**:
   Depending on your desired level of functionality, select one of the following files:
   - `simple_chat.py`
   - `chat_with_session_state.py`
   - `chat_with_mongodb.py`

2. **Run the Streamlit app**:
   ```bash
   streamlit run <script-name>.py
   ```

   For example, to run the full-featured app:
   ```bash
   streamlit run chat_with_mongodb.py
   ```

3. **Access the app**:
   Open the link provided by Streamlit, typically `http://localhost:8501/`.

## How to Use the Application

1. **Start a New Chat**:
   Use the sidebar to create a new chat session.

2. **Continue Previous Chats**:
   Select a previous session from the dropdown in the sidebar.

3. **Interact with the Assistant**:
   Type your messages in the input box, and view the assistant's responses in real time.

4. **Streaming Responses**:
   Watch as the assistant streams its response piece by piece, mimicking a conversational flow.

5. **Persistent Storage**:
   All chat messages are stored in MongoDB, enabling retrieval of previous conversations even after restarting the app.

## Troubleshooting

1. **MongoDB Connection Errors**:
   - Ensure Docker is running and the container is up.
   - Check the `docker-compose.yml` configuration.

2. **Streamlit App Not Running**:
   - Verify that dependencies are installed.
   - Check for typos in the script name.

3. **Ollama Errors**:
   - Ensure Ollama is installed and configured on your system.
   - Test the Ollama setup separately to confirm functionality.

4. **Port Conflicts**:
   - If `localhost:8501` is already in use, run Streamlit on a different port:
     ```bash
     streamlit run <script-name>.py --server.port <new-port>
     ```

---
