import os
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

INPUT_FILE = "output_quill/Deadpool_Wolverine_Novelization_Book1_Start.txt"
OUTPUT_DOCX = "output_quill/Deadpool_Wolverine_Novelization_Book1_Start.docx"
OUTPUT_DOC = "output_quill/Deadpool_Wolverine_Novelization_Book1_Start.doc"
OUTPUT_PDF = "output_quill/Deadpool_Wolverine_Novelization_Book1_Start.pdf"

def create_docx(text, filepath):
    doc = Document()
    for line in text.split('\n'):
        doc.add_paragraph(line)
    doc.save(filepath)
    print(f"Saved {filepath}")

def create_pdf(text, filepath):
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter
    y = height - 40
    c.setFont("Helvetica", 12)

    for line in text.split('\n'):
        # Simple wrapping
        lines = simpleSplit(line, "Helvetica", 12, width - 80)
        for subline in lines:
            if y < 40:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 40
            c.drawString(40, y, subline)
            y -= 14
        y -= 6 # Extra space for paragraph break

    c.save()
    print(f"Saved {filepath}")

def main():
    if not os.path.exists(INPUT_FILE):
        print("Input file not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # DOCX
    create_docx(content, OUTPUT_DOCX)

    # DOC (Renamed DOCX)
    import shutil
    shutil.copy(OUTPUT_DOCX, OUTPUT_DOC)
    print(f"Saved {OUTPUT_DOC}")

    # PDF
    create_pdf(content, OUTPUT_PDF)

if __name__ == "__main__":
    main()
