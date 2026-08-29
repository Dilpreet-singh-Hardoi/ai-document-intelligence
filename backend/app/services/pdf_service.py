import pymupdf


def extract_text_from_pdf(file_path: str) -> str:
    document = pymupdf.open(file_path)

    pages = []

    try:
        for page in document:
            text = page.get_text()

            if text.strip():
                pages.append(text.strip())

        return "\n\n".join(pages)

    finally:
        document.close()