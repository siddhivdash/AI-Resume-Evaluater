import streamlit as st
import pdfplumber
from utils import query_grok_api

# Set up Streamlit page config
st.set_page_config(page_title="AI Resume Evaluater", page_icon="📄", layout="centered")

# Streamlit UI Title
st.title("📄 AI Resume Evaluator")

# File uploader for PDF
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    # Show extracted text
    st.subheader("Extracted Resume Text")
    st.text_area("Text from PDF:", text, height=300)

    # When the user clicks 'Analyze Resume'
    if st.button("Analyze Resume"):
        with st.spinner('Analyzing with AI...'):
            try:
                prompt = f"Analyze this resume text and give detailed feedback on improvements:\n\n{text}"
                feedback = query_grok_api(prompt)
                st.success("Analysis complete!")
                st.subheader("📝 Resume Feedback:")
                st.write(feedback)
            except Exception as e:
                st.error(f"Error: {str(e)}")
