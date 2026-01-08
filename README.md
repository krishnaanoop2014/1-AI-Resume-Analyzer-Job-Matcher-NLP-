# AI Resume Analyzer & Job Matching System

An end-to-end NLP-based application that analyzes resumes and matches them with job descriptions using text similarity techniques. This project demonstrates practical Natural Language Processing (NLP), data preprocessing, and deployment-ready AI application development.

---

## 🚀 Features
- Upload resume text
- Paste job description
- Calculate match percentage
- Identify missing skills
- Clean and simple UI
- Deployable as a web app

---

## 🧠 Tech Stack
- Python
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit

---

## 📊 How It Works
1. Resume and job description text are cleaned and preprocessed
2. TF-IDF converts text into numerical vectors
3. Cosine similarity calculates how closely the resume matches the job
4. Skill gaps are identified using keyword comparison

---

## 📂 Dataset / Data Source
No external dataset required.

You can:
- Use your own resume
- Use sample job descriptions from:
  - https://www.kaggle.com/datasets
  - https://www.indeed.com
  - https://www.linkedin.com/jobs

Sample text files are provided in the `data/` folder.

---

## 🛠 Installation & Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
