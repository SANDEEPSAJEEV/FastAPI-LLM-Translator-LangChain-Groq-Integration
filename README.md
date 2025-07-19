# 🌐 FastAPI LLM Translator: LangChain + Groq Integration

This project is a simple API service built with **FastAPI**, powered by **LangChain** and **Groq’s `gemma2-9b-it`** language model. It provides a translation service that converts input text into **French**.

---

## 🚀 Features

- Built with FastAPI for high-performance async APIs
- Uses `langchain` and `langserve` for modular LLM workflows
- Powered by Groq's blazing-fast `gemma2-9b-it` model
- Environment variable support using `.env`
- Extensible for future use cases like summarization, Q&A, etc.

---

## 🔧 Technologies Used

- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [Groq API](https://console.groq.com/)
- [LangServe](https://github.com/langchain-ai/langserve)
- Uvicorn

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/fastapi-llm-translator.git
cd fastapi-llm-translator

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


pip install -r requirements.txt

Create a .env file in the root directory with the following:

GROQ_API_KEY=your_groq_api_key_here


▶️ Running the Server
python serve.py

