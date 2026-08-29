from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.document import Document
from app.services.storage_service import save_document


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"],
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required",
        )

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are currently supported",
        )

    file_content = await file.read()

    storage_path = save_document(
        file_content=file_content,
        original_filename=file.filename,
    )

    document = Document(
        filename=file.filename,
        file_type=file.content_type,
        file_size=len(file_content),
        storage_path=storage_path,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "id": document.id,
        "filename": document.filename,
        "file_type": document.file_type,
        "file_size": document.file_size,
        "created_at": document.created_at,
    }