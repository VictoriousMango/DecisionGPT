# 🚀 DecisionGPT: GenAI Decision Intelligence System

DecisionGPT is a modular Generative AI system that combines Retrieval-Augmented Generation (RAG), agent-based routing, and data analytics to deliver intelligent, data-driven decisions.

---

## 🧠 Core Idea

The system dynamically routes user queries between:
- 📄 Knowledge retrieval (RAG)
- 📊 Data analytics (CSV insights)
- 🤖 Agent-based reasoning

---

## 🏗️ Architecture

See: `docs/architecture.md`

---

## ⚙️ Tech Stack

- LLM: Groq  
- Framework: LangChain  
- Vector DB: FAISS  
- Backend: FastAPI  
- Frontend: Streamlit  
- Data: Pandas  

---

## 📁 Project Structure
- api/ → FastAPI backend
- ui/ → Streamlit frontend
- rag/ → RAG pipeline
- agents/ → Query routing
- analytics/ → Data processing

---

## 🚀 Setup

```bash pip install -r requirements.txt```

Run backend:
```bash uvicorn api.main:app --reload```

Run frontend:
```bash streamlit run ui/app.py```