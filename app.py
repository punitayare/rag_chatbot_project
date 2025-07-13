import streamlit as st
from ingest import load_and_semantic_chunk
from embed import build_or_load_vectorstore
from groq import ask_groq, get_relevant_context

# --------- Streamlit UI Configuration --------- #
st.set_page_config(page_title="Smart HR Chatbot", page_icon="🤖")
st.title("🤖 Internal HR Chatbot (RAG-Powered)")
st.caption("Ask anything from your internal documents.")

# Load & Prepare Documents
chunks = load_and_semantic_chunk("docs/text.pdf")
retriever = build_or_load_vectorstore(chunks)

# User Input
query = st.text_input("🔍 Ask a question:")

# Answer Generation
if query:
    context, sources = get_relevant_context(retriever, query)
    answer = ask_groq(query, context)

    st.markdown("### 📄 Answer")
    st.write(answer)

    with st.expander("🧠 Retrieved Context"):
        for i, (doc, meta) in enumerate(sources):
            st.markdown(f"**Chunk {i+1} (Page {meta.get('page', 'N/A')}):**")
            st.write(doc)
