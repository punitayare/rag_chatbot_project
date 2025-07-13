# query.py
import requests

def ask_groq(query, context, model="llama3-8b-8192"):
    prompt = f"""
You are a helpful, polite, and professional HR assistant. Answer based on the provided context only.

[Context]
{context}

[Question]
{query}

[Answer]
"""
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

def get_relevant_context(retriever, query):
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    sources = [(doc.page_content, doc.metadata) for doc in docs]
    return context, sources
