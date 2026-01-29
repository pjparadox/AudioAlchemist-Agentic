from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
import os
import shutil
import re

def create_manuscript():
    # Input files - Expanded List
    files = [
        "context/projects/Emily_Rose_Novelization/output_quill/Part_1_Chapters_1-5.txt",
        "context/projects/Emily_Rose_Novelization/output_quill/Part_1_Chapters_6-10.txt",
        "context/projects/Emily_Rose_Novelization/output_quill/Part_2_Chapters_11-15.txt",
        "context/projects/Emily_Rose_Novelization/output_quill/Part_2_Chapters_16-20.txt",
        # Re-using previous dense chapters for Part III & IV logic to complete narrative arc
        # Renaming the content flow to match the new structure in the final assembly
        "context/projects/Emily_Rose_Novelization/output_quill/Chapter_13_18.txt",
        "context/projects/Emily_Rose_Novelization/output_quill/Chapter_19_23.txt"
    ]

    # 1. Create Consolidated Text File
    full_text = ""
    for f in files:
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8') as infile:
                content = infile.read()
                full_text += content + "\n\n"
        else:
            print(f"Warning: {f} not found.")

    output_txt = "context/projects/Emily_Rose_Novelization/output_quill/The_Exorcism_of_Emily_Rose_Epic_Novel.txt"
    with open(output_txt, 'w', encoding='utf-8') as out:
        out.write(full_text)
    print(f"Created {output_txt}")

    # 2. Create DOCX
    doc = Document()
    doc.add_heading('The Exorcism of Emily Rose', 0)
    doc.add_paragraph('A Novelization')
    doc.add_paragraph('By Jules (Agent Suite)')
    doc.add_page_break()

    for line in full_text.split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith('# Chapter') or line.startswith('***'):
            clean_line = line.replace('# ', '').replace('***', '').strip()
            if clean_line:
                doc.add_heading(clean_line, level=1)
        elif line.startswith('## Chapter'):
             clean_line = line.replace('## ', '').strip()
             doc.add_heading(clean_line, level=1)
        elif line.startswith('*Flashback*') or line.startswith('*Present Day*'):
             doc.add_heading(line, level=2)
        else:
            doc.add_paragraph(line)

    docx_path = "context/projects/Emily_Rose_Novelization/output_quill/The_Exorcism_of_Emily_Rose_Epic_Novel.docx"
    doc.save(docx_path)
    print(f"Created {docx_path}")

    # 3. Create DOC
    doc_path = "context/projects/Emily_Rose_Novelization/output_quill/The_Exorcism_of_Emily_Rose_Epic_Novel.doc"
    shutil.copy(docx_path, doc_path)
    print(f"Created {doc_path}")

    # 4. Create PDF
    pdf_path = "context/projects/Emily_Rose_Novelization/output_quill/The_Exorcism_of_Emily_Rose_Epic_Novel.pdf"

    doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    Story = []
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(name='Justified', alignment=TA_JUSTIFY, fontSize=11, leading=14))
    styles.add(ParagraphStyle(name='ChapterHeader', parent=styles['Heading1'], alignment=TA_CENTER, fontSize=16, spaceAfter=20))
    styles.add(ParagraphStyle(name='SceneHeader', parent=styles['Heading2'], alignment=TA_CENTER, fontSize=12, spaceBefore=10, spaceAfter=10))

    Story.append(Paragraph("The Exorcism of Emily Rose", styles['Title']))
    Story.append(Spacer(1, 12))
    Story.append(Paragraph("A Novelization", styles['Normal']))
    Story.append(PageBreak())

    for line in full_text.split('\n'):
        line = line.strip()
        if not line:
            Story.append(Spacer(1, 6))
            continue

        if line.startswith('# Chapter') or line.startswith('***') or line.startswith('## Chapter'):
            clean_line = line.replace('# ', '').replace('## ', '').replace('***', '').strip()
            if clean_line:
                Story.append(PageBreak())
                Story.append(Paragraph(clean_line, styles['ChapterHeader']))
        elif line.startswith('*Flashback*') or line.startswith('*Present Day*'):
            Story.append(Paragraph(line, styles['SceneHeader']))
        else:
            line = re.sub(r'\*([^\*]+)\*', r'<i>\1</i>', line)
            Story.append(Paragraph(line, styles['Justified']))

    doc.build(Story)
    print(f"Created {pdf_path}")

if __name__ == "__main__":
    create_manuscript()
