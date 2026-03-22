from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

DB_PATH = "faiss_index"


def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)


def get_answer(query):
    db = load_vector_store()
    retriever = db.as_retriever(search_kwargs={"k": 3})

    docs = retriever.invoke(query)  # ✅ replaces deprecated get_relevant_documents()
    context = "\n".join([doc.page_content for doc in docs])

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

    prompt = f"""
You are a business decision assistant.

Use ONLY the provided context to answer.

If the answer is not in context, say "Not enough information".

Context:
{context}

Question:
{query}

Answer clearly with reasoning:
"""

    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    while True:
        query = input("Ask: ")
        answer = get_answer(query)
        print("\nAnswer:", answer)
        break