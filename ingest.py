 langchain.document_loaders import PyMuPDFLoader
from langchain.schema import Document
import nltk
from sentence_transformers import SentenceTransformer
import streamlit as st

# Ensure required data is downloaded
nltk.download('punkt')

# Load the SentenceTransformer model
semantic_model = SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_resource
def load_and_semantic_chunk(pdf_path, chunk_size=500, chunk_overlap=50):
    loader = PyMuPDFLoader(pdf_path)
    raw_documents = loader.load()

    chunked_docs = []
    for doc in raw_documents:
        sentences = nltk.sent_tokenize(doc.page_content)
        current_chunk = []
        current_length = 0

        for sentence in sentences:
            sentence_length = len(sentence)
            if current_length + sentence_length <= chunk_size:
                current_chunk.append(sentence)
                current_length += sentence_length
            else:
                # Save the current chunk
                chunk_text = " ".join(current_chunk)
                chunked_docs.append(Document(page_content=chunk_text, metadata=doc.metadata))
                
                # Start a new chunk with overlap
                overlap = " ".join(current_chunk[-1:])  # Last sentence as overlap
                current_chunk = [overlap, sentence]
                current_length = len(overlap) + sentence_length

        # Append any remaining chunk
        if current_chunk:
            chunk_text = " ".join(current_chunk)
            chunked_docs.append(Document(page_content=chunk_text, metadata=doc.metadata))

    return chunked_docs
