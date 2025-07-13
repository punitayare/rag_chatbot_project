# 📄 RAG Chatbot for Internal Document Question Answering

This project is a **Retrieval-Augmented Generation (RAG)** chatbot designed to answer natural language queries from internal PDF documents. It combines:

- Semantic chunking with **Sentence Transformers**
- Embeddings via **BAAI/bge-base-en-v1.5**
- **FAISS** for fast vector search
- Fast LLM generation using the **Groq API**
- A clean **Streamlit UI**

---

## 🚀 Live Demo

🔗 [Try the App](https://ragchatbotprojectgit-xx4jrh9dcpqunyrrprrkx8.streamlit.app/)  
📦 [GitHub Repo](https://github.com/punitayare/rag_chatbot_project.git)

---

## 📂 Project Structure

```plaintext
rag_chatbot_project/
│
├── app.py                  # Streamlit UI
├── ingest.py               # PDF loader and semantic chunker
├── embed.py                # Embedding + vectorstore builder
├── query.py                # Groq LLM querying logic
├── .env                    # Stores GROQ_API_KEY 
├── requirements.txt        # All Python dependencies
└── README.md               # This file
```
## ⚙️ Installation & Setup
1. Clone the Repository
```plaintext
git clone https://github.com/punitayare/rag_chatbot_project.git
cd rag_chatbot_project
```
2. Create and Activate a Virtual Environment (Optional)

## On Windows:
```plaintext
python -m venv venv
venv\Scripts\activate
```

## On macOS/Linux:
```plaintext
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```plaintext
pip install -r requirements.txt
```
4. Add Your Groq API Key
Create a .env file in the root folder and add your key:
```plaintext
GROQ_API_KEY=your_groq_api_key_here
```


▶️ Run the App Locally
```plaintext
streamlit run app.py
Visit http://localhost:8501 in your browser.
```
💬 Example Questions to Try

What is the leave policy mentioned in the document?

How many sick leaves are allowed annually?

What are the disciplinary actions listed?

✅ Requirements
```plaintext
Python 3.9+

streamlit

langchain

sentence-transformers

transformers

faiss-cpu

pymupdf

python-dotenv

requests
```
