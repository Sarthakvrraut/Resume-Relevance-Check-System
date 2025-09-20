# ------------------------------------------------------------
# © 2025 Sarthak Raut
# Resume Relevance Check System
# All rights reserved. Unauthorized copying, modification,
# or distribution of this file is prohibited.
# ------------------------------------------------------------

from resume_parser import parse_resume
import re

def extract_jd_keywords(jd_text):
    # Simple regex-based skill extraction (can be enhanced with spaCy NER)
    skills = re.findall(r'\b[A-Za-z0-9\+\#]+\b', jd_text)
    return list(set(skills))
