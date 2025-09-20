from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os

# Create folder for sample resumes
os.makedirs("sample_resumes", exist_ok=True)

# Sample candidates
candidates = [
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "phone": "+91 9876543210",
        "linkedin": "https://linkedin.com/in/alicejohnson",
        "education": [
            {"degree": "B.Tech in Computer Science", "institution": "IIT Delhi", "year": "2022", "cgpa": "9.1/10"},
            {"degree": "High School", "institution": "Delhi Public School", "year": "2018", "cgpa": "95%"}
        ],
        "skills": ["Python", "Machine Learning", "Data Analysis", "SQL", "Pandas", "NumPy", "TensorFlow", "PyTorch"],
        "certifications": ["AWS Certified Solutions Architect", "Google Data Analytics Certificate"],
        "projects": [
            {"title": "Stock Price Prediction", "description": "Built a ML model using LSTM networks to predict stock prices with 92% accuracy."},
            {"title": "Chatbot Development", "description": "Developed a customer support chatbot using NLP techniques and deployed on a web platform."}
        ],
        "experience": [
            {"role": "Data Science Intern", "company": "Tech Solutions Pvt Ltd", "duration": "Jun 2021 - Aug 2021", "details": "Worked on predictive analytics models and dashboards."}
        ]
    },
    {
        "name": "Bob Smith",
        "email": "bob.smith@example.com",
        "phone": "+91 9123456780",
        "linkedin": "https://linkedin.com/in/bobsmith",
        "education": [
            {"degree": "B.Tech in Information Technology", "institution": "VIT Pune", "year": "2023", "cgpa": "8.7/10"},
            {"degree": "High School", "institution": "St. Xavier's School", "year": "2019", "cgpa": "93%"}
        ],
        "skills": ["Java", "Spring Boot", "REST APIs", "MySQL", "Microservices", "Docker", "Kubernetes"],
        "certifications": ["Oracle Certified Java Programmer", "Certified Kubernetes Administrator"],
        "projects": [
            {"title": "E-commerce Web App", "description": "Designed and implemented a full-stack e-commerce platform with payment integration."},
            {"title": "Inventory Management System", "description": "Developed system to track stock levels and automate order processing."}
        ],
        "experience": [
            {"role": "Backend Developer Intern", "company": "Innovatech Solutions", "duration": "May 2022 - Jul 2022", "details": "Implemented REST APIs and optimized database queries."}
        ]
    }
]

# Function to safely render text
def safe_multicell(pdf, text, w=0, h=6):
    """
    Splits long words to avoid FPDFException: Not enough horizontal space.
    """
    max_char_per_line = 80
    words = text.split(' ')
    new_text = ''
    for word in words:
        while len(word) > max_char_per_line:
            new_text += word[:max_char_per_line] + '-\n'
            word = word[max_char_per_line:]
        new_text += word + ' '
    pdf.multi_cell(w, h, new_text.strip())

# Generate resumes
for i, candidate in enumerate(candidates, start=1):
    pdf = FPDF(format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Header: Name
    pdf.set_font("Helvetica", 'B', 24)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, candidate["name"], new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

    # Contact info
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(0, 0, 0)
    safe_multicell(pdf, f"Email: {candidate['email']} | Phone: {candidate['phone']} | LinkedIn: {candidate['linkedin']}")
    pdf.ln(5)

    # Section: Education
    pdf.set_font("Helvetica", 'B', 16)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 8, "Education", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(0, 0, 0)
    for edu in candidate['education']:
        safe_multicell(pdf, f"{edu['degree']} - {edu['institution']} ({edu['year']}) | CGPA: {edu['cgpa']}")
    pdf.ln(3)

    # Section: Skills
    pdf.set_font("Helvetica", 'B', 16)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 8, "Skills", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(0, 0, 0)
    safe_multicell(pdf, ", ".join(candidate['skills']))
    pdf.ln(3)

    # Section: Certifications
    pdf.set_font("Helvetica", 'B', 16)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 8, "Certifications", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(0, 0, 0)
    for cert in candidate['certifications']:
        safe_multicell(pdf, f"- {cert}")
    pdf.ln(3)

    # Section: Projects
    pdf.set_font("Helvetica", 'B', 16)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 8, "Projects", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(0, 0, 0)
    for proj in candidate['projects']:
        safe_multicell(pdf, f"{proj['title']}: {proj['description']}")
    pdf.ln(3)

    # Section: Experience
    pdf.set_font("Helvetica", 'B', 16)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 8, "Experience", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(0, 0, 0)
    for exp in candidate['experience']:
        safe_multicell(pdf, f"{exp['role']} at {exp['company']} ({exp['duration']}): {exp['details']}")
    pdf.ln(3)

    # Save PDF
    pdf_file = f"sample_resumes/resume_{i}.pdf"
    pdf.output(pdf_file)

print("Professional sample resumes generated in 'sample_resumes/' folder successfully!")
