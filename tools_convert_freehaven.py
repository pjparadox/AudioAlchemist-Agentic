import os
import re
import shutil
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

INPUT_FILE = "output_quill/Freehaven_Online_Full_Novel-vn.txt"
OUTPUT_DIR = "output_quill"
BASE_NAME = "Freehaven_Online_Full_Novel-vn"

# Register Font for Vietnamese support in PDF
FONT_PATH = "foundation/fonts/DejaVuSans.ttf"
BOLD_FONT_PATH = "foundation/fonts/DejaVuSans-Bold.ttf"

if os.path.exists(FONT_PATH) and os.path.exists(BOLD_FONT_PATH):
    pdfmetrics.registerFont(TTFont('DejaVuSans', FONT_PATH))
    pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', BOLD_FONT_PATH))
    FONT_NAME = 'DejaVuSans'
    BOLD_FONT_NAME = 'DejaVuSans-Bold'
else:
    print("Warning: DejaVuSans font not found. Vietnamese text may not render correctly in PDF.")
    FONT_NAME = 'Helvetica'
    BOLD_FONT_NAME = 'Helvetica-Bold'

def parse_markdown_line(line):
    """Parses a line of text for bold (**) and italic (*) markdown."""
    parts = []
    current_text = ""
    i = 0
    n = len(line)
    is_bold = False
    is_italic = False

    while i < n:
        if line[i:i+2] == '**':
            if current_text:
                parts.append((current_text, is_bold, is_italic))
                current_text = ""
            is_bold = not is_bold
            i += 2
            continue

        if line[i] == '*':
            if current_text:
                parts.append((current_text, is_bold, is_italic))
                current_text = ""
            is_italic = not is_italic
            i += 1
            continue

        current_text += line[i]
        i += 1

    if current_text:
        parts.append((current_text, is_bold, is_italic))

    return parts

def create_docx(text, filepath):
    doc = Document()
    doc.add_heading('Freehaven Online', 0)

    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith('#'):
            level = line.count('#')
            clean_line = line.replace('#', '').strip()
            if level > 9: level = 9
            doc.add_heading(clean_line, level=level)
        else:
            p = doc.add_paragraph()
            segments = parse_markdown_line(line)
            for text_segment, bold, italic in segments:
                run = p.add_run(text_segment)
                if bold: run.bold = True
                if italic: run.italic = True

    doc.save(filepath)
    print(f"Saved DOCX: {filepath}")

def create_pdf(text, filepath):
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()

    styles['Normal'].fontName = FONT_NAME
    styles['Normal'].fontSize = 12
    styles['Heading1'].fontName = BOLD_FONT_NAME
    styles['Heading2'].fontName = BOLD_FONT_NAME
    styles['Title'].fontName = BOLD_FONT_NAME

    story = []
    story.append(Paragraph("Freehaven Online", styles['Title']))
    story.append(Spacer(1, 24))

    for line in text.split('\n'):
        line = line.strip()
        if not line:
            story.append(Spacer(1, 12))
            continue

        if line.startswith('#'):
            level = line.count('#')
            clean_text = line.replace('#', '').strip()
            style = styles['Heading1'] if level == 1 else styles['Heading2']
            story.append(Paragraph(clean_text, style))
        else:
            formatted_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            formatted_line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', formatted_line)
            story.append(Paragraph(formatted_line, styles['Normal']))

    doc.build(story)
    print(f"Saved PDF: {filepath}")

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    docx_path = os.path.join(OUTPUT_DIR, BASE_NAME + ".docx")
    create_docx(content, docx_path)

    doc_path = os.path.join(OUTPUT_DIR, BASE_NAME + ".doc")
    shutil.copy(docx_path, doc_path)
    print(f"Saved DOC: {doc_path}")

    pdf_path = os.path.join(OUTPUT_DIR, BASE_NAME + ".pdf")
    create_pdf(content, pdf_path)

if __name__ == "__main__":
    main()
