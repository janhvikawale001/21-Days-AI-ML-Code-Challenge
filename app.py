import streamlit as st
from transformers import pipeline

st.title("🚀 AI-Powered Text Summarizer")

# Load model (cached so it doesn't reload every time)
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# Text input
text = st.text_area("Paste your long article here:", height=200)

# Generate button
if st.button("Generate Summary"):
    if text:
        with st.spinner("Generating summary..."):
            summary = summarizer(
                text,
                max_length=100,
                min_length=30,
                do_sample=False
            )
        st.subheader("📌 Summary:")
        st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter text first.")
