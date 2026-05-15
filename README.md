# Streamlit LangGraph Chatbot

A simple chatbot built using **Streamlit**, **LangGraph**, and **Hugging Face Llama 3.1** with conversation memory using LangGraph checkpoints.

---

## Features

* Interactive chatbot UI using Streamlit
* Built with LangGraph state-based workflow
* Hugging Face LLM integration
* In-memory conversation persistence
* Thread-based chat memory

---

## Tech Stack

* Python
* Streamlit
* LangGraph
* LangChain
* Hugging Face
* dotenv

---

## Project Structure

```bash
langraph_chatbot/
│── streamlit_frontend.py
│── langraph_backend.py
│── .env
│── requirements.txt
```

---

## Installation

### 1. Clone repository

```bash
git clone <repository-url>
cd langraph_chatbot
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
HUGGINGFACEHUB_ACCESS_TOKEN=your_token_here
```

---

## Run the Application

```bash
streamlit run streamlit_frontend.py
```

---

## How It Works

### Backend

* Defines chatbot state using `TypedDict`
* Creates LangGraph workflow
* Stores conversation using `InMemorySaver`
* Sends user messages to Hugging Face Llama model

### Frontend

* Accepts user input
* Sends input to LangGraph backend
* Displays chatbot responses
* Maintains session state

---

## Example Workflow

```text
User Input
   ↓
Streamlit Frontend
   ↓
LangGraph StateGraph
   ↓
Chat Node
   ↓
Hugging Face Model
   ↓
Response Displayed
```

---

## Future Improvements

* Add SQLite persistent checkpoints
* Add multiple chat threads
* Add RAG support
* Deploy on Streamlit Cloud
* Add custom system prompts

---

