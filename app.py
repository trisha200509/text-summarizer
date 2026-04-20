import streamlit as st

st.title("📝 Text Summarizer")

st.write("This project summarizes long text into short meaningful content using NLP techniques.")

text = st.text_area("Enter your text here:")

def simple_summarize(text):
    sentences = text.split(".")
    summary = ". ".join(sentences[:2])  # first 2 sentences
    return summary

if st.button("Summarize"):
    if text.strip() != "":
        summary = simple_summarize(text)
        st.subheader("📌 Summary:")
        st.success(summary)
    else:
        st.warning("Please enter some text.")