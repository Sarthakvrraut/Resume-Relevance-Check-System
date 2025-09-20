import sqlite3

def init_db():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evaluations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_name TEXT,
        jd_name TEXT,
        score REAL,
        verdict TEXT,
        missing_skills TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_evaluation(resume_name, jd_name, score, verdict, missing_skills):
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO evaluations (resume_name, jd_name, score, verdict, missing_skills)
    VALUES (?, ?, ?, ?, ?)
    """, (resume_name, jd_name, score, verdict, ",".join(missing_skills)))
    conn.commit()
    conn.close()
