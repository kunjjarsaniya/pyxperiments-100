# pip install streamlit reportlab

# -------------------------------------------------------------
# 📄 Enhanced Resume Builder with PDF Export (Streamlit + OOP)
# -------------------------------------------------------------

import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from io import BytesIO

# -------------------------------------------------------------
# 📦 ResumeData Class – Stores resume fields
# -------------------------------------------------------------

class ResumeData:
    def __init__(self, name, about, skills, projects, education, experience):
        self.name = name
        self.about = about
        self.skills = skills
        self.projects = projects
        self.education = education
        self.experience = experience

    def to_text(self):
        return f"""
===================================
📄 Resume - {self.name}
===================================

👤 About:
{self.about}

🛠️ Skills:
{self.skills}

📁 Projects:
{self.projects}

🎓 Education:
{self.education}

💼 Experience:
{self.experience}
"""

# -------------------------------------------------------------
# 📁 ResumeManager Class – Save as text and PDF
# -------------------------------------------------------------

class ResumeManager:
    def __init__(self, directory="resumes"):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def save_txt(self, resume: ResumeData):
        filepath = os.path.join(self.directory, f"{resume.name.replace(' ', '_')}_resume.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(resume.to_text())
        return filepath

    def generate_pdf(self, resume: ResumeData) -> BytesIO:
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        y = height - 40
        line_gap = 18

        def draw_line(text):
            nonlocal y
            for line in text.splitlines():
                if line.strip():
                    c.drawString(40, y, line.strip())
                    y -= line_gap

        c.setFont("Helvetica-Bold", 16)
        c.drawString(40, y, f"Resume - {resume.name}")
        y -= 30

        c.setFont("Helvetica", 12)
        draw_line(f"👤 About:\n{resume.about}\n")
        draw_line(f"🛠️ Skills:\n{resume.skills}\n")
        draw_line(f"📁 Projects:\n{resume.projects}\n")
        draw_line(f"🎓 Education:\n{resume.education}\n")
        draw_line(f"💼 Experience:\n{resume.experience}\n")

        c.showPage()
        c.save()
        buffer.seek(0)
        return buffer

# -------------------------------------------------------------
# 🖼️ Streamlit App Interface
# -------------------------------------------------------------

def main():
    st.set_page_config(page_title="📄 Resume Builder with PDF", layout="centered")
    st.title("📄 Resume Builder with PDF Export")
    st.markdown("Fill out the details below and download your resume as PDF or TXT.")

    with st.form("resume_form"):
        name = st.text_input("👤 Full Name")
        about = st.text_area("📌 About You")
        skills = st.text_area("🛠️ Skills (comma-separated)")
        projects = st.text_area("📁 Projects")
        education = st.text_area("🎓 Education")
        experience = st.text_area("💼 Experience")
        submitted = st.form_submit_button("✅ Generate Resume")

    if submitted:
        if not name.strip():
            st.error("Please enter your name.")
            return

        resume = ResumeData(name, about, skills, projects, education, experience)
        manager = ResumeManager()

        # Display Resume Text
        st.markdown("### 📄 Resume Preview")
        st.text(resume.to_text())

        # Save as TXT
        txt_path = manager.save_txt(resume)
        st.success(f"💾 Text Resume Saved: `{txt_path}`")

        # Generate and Download PDF
        pdf_data = manager.generate_pdf(resume)
        st.download_button(
            label="📥 Download as PDF",
            data=pdf_data,
            file_name=f"{name.replace(' ', '_')}_resume.pdf",
            mime="application/pdf"
        )

# -------------------------------------------------------------
# 🚀 Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    main()
