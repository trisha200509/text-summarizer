import streamlit as st
from PyPDF2 import PdfReader

# Title
st.title("📝 AI Text Summarizer")

st.markdown("---")

# PDF Upload
uploaded_file = st.file_uploader("📄 Upload a PDF file", type="pdf")

text = ""

# Extract text from PDF
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

# Manual text input
text_input = st.text_area("✍️ Or enter your text here:")

# Choose input
final_text = text if text else text_input

# Simple summarizer function
def simple_summarize(text):
    sentences = text.split(".")
    summary = ". ".join(sentences[:2])  # first 2 sentences
    return summary

# Button
if st.button("🔍 Summarize"):
    if final_text.strip() != "":
        summary = simple_summarize(final_text)
        st.subheader("📌 Summary:")
        st.success(summary)
    else:
        st.warning("Please enter text or upload a PDF")

# Footer
st.markdown("---")
st.caption("🚀 Deployed using Streamlit Cloud")