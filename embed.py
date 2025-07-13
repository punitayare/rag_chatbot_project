# embed.py
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import streamlit as st

@st.cache_resource
def build_or_load_vectorstore(_docs, persist_path="vector_index"):
    embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    vectorstore = FAISS.from_documents(_docs, embedding_model)
    vectorstore.save_local(persist_path)
    return vectorstore.as_retriever(search_kwargs={"k": 4})
