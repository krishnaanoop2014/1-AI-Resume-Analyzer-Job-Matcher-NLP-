import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# ------------------ Text Cleaning ------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

# ------------------ Skill Extraction ------------------
def extract_skills(text, skill_list):
    text = text.lower()
    found_skills = [skill for skill in skill_list if skill in text]
    return found_skills

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & Job Matcher")
st.write("Match your resume with a job description using NLP")

resume_text = st.text_area("Paste Resume Text Here", height=200)
job_text = st.text_area("Paste Job Description Here", height=200)

if st.button("Analyze"):
    if resume_text and job_text:
        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_text)

        documents = [resume_clean, job_clean]

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_percentage = round(similarity * 100, 2)

        st.subheader("📊 Match Result")
        st.success(f"Resume Match Score: **{match_percentage}%**")

        # Skill analysis
        skills = [
            "python", "machine learning", "data analysis",
            "deep learning", "sql", "nlp", "tensorflow",
            "pandas", "numpy", "scikit learn"
        ]

        resume_skills = extract_skills(resume_clean, skills)
        job_skills = extract_skills(job_clean, skills)

        missing_skills = list(set(job_skills) - set(resume_skills))

        st.subheader("🧠 Skill Analysis")
        st.write("**Skills Found in Resume:**", resume_skills)
        st.write("**Skills Required by Job:**", job_skills)
        st.warning(f"**Missing Skills:** {missing_skills}")

    else:
        st.error("Please paste both resume and job description.")
