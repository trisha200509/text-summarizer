import streamlit as st
from PyPDF2 import PdfReader

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Page config
st.set_page_config(page_title="Text Summarizer", page_icon="🧠", layout="wide")

# 🌈 INSANE CSS
st.markdown("""
<style>
.main-title {
    font-size: 50px;
    font-weight: bold;
    background: linear-gradient(90deg, #6366f1, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 30px;
}
.glass {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# 🧭 Sidebar
st.sidebar.title("⚙️ Controls")

mode = st.sidebar.radio("Input Type:", ["Text", "PDF"])
length = st.sidebar.slider("Summary Length", 1, 5, 2)

st.sidebar.markdown("---")
st.sidebar.caption("🚀 Text Summarizer")

# 🏷️ Title
st.markdown('<div class="main-title">🧠 Text Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Next-gen text summarization app</div>', unsafe_allow_html=True)

# 📄 Input
text = ""

if mode == "PDF":
    st.markdown("### 📄 Upload PDF")
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

    if uploaded_file:
        reader = PdfReader(uploaded_file)
        for page in reader.pages[:5]:
            if page.extract_text():
                text += page.extract_text()

else:
    st.markdown("### ✍️ Enter Text")
    text = st.text_area("Paste your text here", height=200)

# 🧠 Summarizer
def summarize_text(text, lines=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, lines)

    final_summary = ""
    for sentence in summary:
        final_summary += str(sentence) + " "

    return final_summary

# 🚀 Generate
if st.button("✨ Generate Summary"):
    if text.strip():
        with st.spinner("🚀 Generating  summary..."):
            summary = summarize_text(text, length)

        st.markdown("### 📌 Summary")
        st.success(summary)

        # 📊 Analytics Dashboard
        words = len(text.split())
        sentences = len(text.split("."))

        col1, col2, col3 = st.columns(3)
        col1.metric("📊 Words", words)
        col2.metric("🧾 Sentences", sentences)
        col3.metric("📌 Summary Length", length)

        # 📥 Download
        st.download_button(
            "📥 Download Summary",
            summary,
            file_name="summary.txt"
        )

        # 📋 Copy
        st.code(summary)

    else:
        st.warning("Please provide input")

# Footer
st.markdown("---")
st.caption("💡 Text summarizer| Mini Project")