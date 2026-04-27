import streamlit as st
import pdfplumber

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

st.title("Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)

    keywords = ["python", "sql", "machine learning", "html", "css"]

    found = []
    missing = []

    for skill in keywords:
        if skill.lower() in text.lower():
            found.append(skill)
        else:
            missing.append(skill)

    score = (len(found) / len(keywords)) * 100

    st.write("### Resume Score:", score)
    st.write("### Skills Found:", found)
    st.write("### Missing Skills:", missing)