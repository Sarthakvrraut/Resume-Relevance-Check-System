from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def hard_match_score(resume_text, jd_keywords):
    score = 0
    resume_words = resume_text.lower().split()
    hits = sum([1 for kw in jd_keywords if kw.lower() in resume_words])
    score = (hits / len(jd_keywords)) * 50  # Hard match weight 50%
    missing = [kw for kw in jd_keywords if kw.lower() not in resume_words]
    return score, missing

def semantic_match_score(resume_text, jd_text, model):
    # Compute embeddings and cosine similarity
    resume_emb = model.encode([resume_text])[0]
    jd_emb = model.encode([jd_text])[0]
    sim = cosine_similarity([resume_emb], [jd_emb])[0][0]
    return sim * 50  # Soft match weight 50%

def final_verdict(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"
