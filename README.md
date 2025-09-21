📄 Resume Relevance Check System
🚀 Problem Statement
Recruiters spend a lot of time scanning resumes to match them against job descriptions. Manual screening is time-consuming, error-prone, and inconsistent.
Goal: Automate the resume screening process by extracting content from resumes (PDF/DOCX) and ranking them against job descriptions using NLP + ML techniques.


🧠 Approach
Data Ingestion
Upload resumes in .pdf / .docx format
Extract text using PyMuPDF & docx2txt
Preprocessing
Tokenization, stopword removal, lemmatization
Keyword extraction from resumes & job description
Feature Engineering
TF-IDF vectorization
Cosine similarity for relevance scoring
ML Model (Scikit-learn)
Train relevance scoring pipeline
Rank resumes by similarity score
Streamlit Web App
Upload resumes + JD
Display results in a ranked table
Download structured report

⚙️ Installation
# Clone the repo
git clone https://github.com/<your-username>/resume-relevance-check-system.git
cd resume-relevance-check-system

# Create virtual environment (Python 3.9+ recommended)
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows

# Install dependencies
pip install -r requirements.txt

▶️ Usage
Run Streamlit app
streamlit run omr_streamlit_app.py
Generate Word report
python generate_docx_report.py
Example Output
Ranks resumes based on job description
Provides similarity scores
Exports .docx report for recruiters

📦 Tech Stack
Python 3.13
Streamlit (Web UI)
PyMuPDF, docx2txt (Text extraction)
Scikit-learn (ML/NLP)
python-docx (Reports)

👨‍💻 Author
© 2025 Sarthak Raut – All rights reserved
