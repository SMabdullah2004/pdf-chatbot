# pdf_utils.py
from PyPDF2 import PdfReader

async def extract_text_from_pdf(file):
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
