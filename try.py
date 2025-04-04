import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

pdf_path = "legal_documents.pdf"

text = extract_text_from_pdf("legal_documents.pdf")
print(text[:1000])  # Preview first 1000 characters
