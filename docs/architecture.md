# 🏗️ DecisionGPT Architecture

## High-Level Flow

User Query
   ↓
Streamlit UI (Frontend)
   ↓
FastAPI Backend
   ↓
Query Router (Agent)
   ↓
----------------------------------
|        System Core             |
|                               |
| 1. RAG Pipeline               |
|    - FAISS Vector DB          |
|    - Embeddings               |
|    - LLM Response             |
|                               |
| 2. Analytics Engine           |
|    - Pandas                   |
|    - Data Insights            |
|                               |
| 3. Agent Layer                |
|    - Query Classification     |
|    - Multi-step Reasoning     |
----------------------------------
   ↓
Final Response (Insight + Answer)