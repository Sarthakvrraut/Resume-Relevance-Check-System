import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_skills(text):
    skills_pattern = r"(Python|Java|SQL|TensorFlow|PyTorch|Docker|Kubernetes|Spring Boot|Pandas|NumPy)"
    return re.findall(skills_pattern, text, re.IGNORECASE)

def compute_relevance(resume_text, jd_text):
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))
    matched_skills = resume_skills & jd_skills
    hard_score = (len(matched_skills) / max(len(dj_skills:=jd_skills), 1)) * 50  # 50% weight

    vectorizer = TfidfVectorizer().fit([resume_text, jd_text])
    vectors = vectorizer.transform([resume_text, jd_text])
    soft_score = cosine_similarity(vectors[0], vectors[1])[0][0] * 50  # 50% weight

    total_score = round(hard_score + soft_score, 2)

    if total_score >= 75:
        verdict = "High"
    elif total_score >= 50:
        verdict = "Medium"
    else:
        verdict = "Low"

    missing_items = list(dj_skills - resume_skills)
    return total_score, verdict, missing_items
