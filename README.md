# Gen-AI

A Simple FastAPI + LangChain AI API Server supporting multiple language models.

This project exposes AI endpoints using **FastAPI** and **LangServe**, including both OpenAI and local LLM integration (via Ollama). It's ideal as a lightweight backend for chatbot apps, AI services or GenAI experimentation.

---

## 🔥 Features

- FastAPI server with Swagger UI  
- LangChain modular architecture  
- OpenAI GPT API support  
- Local LLM support with Ollama  
- Prompt-based AI endpoints  
- Ready for deployment

---

## 🚀 Endpoints

After running the server:

- Swagger Docs: http://localhost:8000/docs  
- OpenAI Chat: http://localhost:8000/openai  
- Essay Generator: http://localhost:8000/essay  
- Ollama Local Model: http://localhost:8000/ollama  

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/abhikghosh2049/Gen-AI
cd Gen-AI
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ▶️ Run the Server

```bash
uvicorn app:app --reload
```

Server runs at:

```
http://localhost:8000
```

---

## 📁 Project Structure

```
Gen-AI/
├── api/
│   └── app.py
├── chatbot/
├── requirements.txt
├── .env
└── .gitignore
```

---

## 🧠 Supported Models

| Model | Platform |
|------|----------|
| OpenAI GPT | Cloud |
| LLaMA2 | Local (Ollama) |

---

## 📌 Notes

- Do not commit `.env`
- Do not commit `venv/`
- Ollama must be running locally for local LLM usage

---

## 📜 License

Open Source

---

## 🙌 Author

**Abhik Ghosh**  
GitHub: https://github.com/abhikghosh2049
