from app.services.pdf_service import extract_text_from_pdf


def process_document(file_path: str) -> str:
    return extract_text_from_pdf(file_path)