from pathlib import Path
from uuid import uuid4


UPLOAD_DIR = Path("storage/documents")


def save_document(file_content: bytes, original_filename: str) -> str:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_extension = Path(original_filename).suffix
    stored_filename = f"{uuid4()}{file_extension}"

    file_path = UPLOAD_DIR / stored_filename
    file_path.write_bytes(file_content)

    return str(file_path)