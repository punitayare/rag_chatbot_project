# 📄 RAG Chatbot for Internal Document Question Answering

This project is a **Retrieval-Augmented Generation (RAG)** chatbot designed to answer natural language queries based on internal PDF documents. It uses SentenceTransformers for embeddings, FAISS for vector storage, and the Groq API for fast and efficient LLM-powered answer generation. The UI is built with **Streamlit** for ease of use.

---

## 🚀 Demo

🔗 **Live App:** [RAG Chatbot Streamlit App](https://ragchatbotprojectgit-xx4jrh9dcpqunyrrprrkx8.streamlit.app/)


---

## 🧠 Features

- Upload internal documents (PDFs)
- Automatic semantic chunking using Sentence Transformers
- Embedding with `BAAI/bge-base-en-v1.5`
- Vector storage with **FAISS**
- Fast responses via **Groq-hosted LLaMA 3** model
- User-friendly interface with **Streamlit**
- Retrieved chunk preview for transparency

---

## 📂 Project Structure

```plaintext
rag_chatbot_project/
│
├── app.py                  # Main Streamlit UI and app logic
├── ingest.py               # PDF loading and semantic chunking
├── embed.py                # Embedding and vector store creation
├── query.py                # Querying Groq LLM with context
├── .env                    # Contains your GROQ_API_KEY (not pushed)
├── requirements.txt        # Python dependencies
└── docs/
    └── text.pdf            # Your input document(s)
