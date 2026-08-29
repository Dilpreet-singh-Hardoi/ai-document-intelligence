from fastapi import FastAPI

from app.api.documents import router as documents_router


app = FastAPI(
    title="AI Document Intelligence API",
    description="AI-powered document analysis and question answering platform",
    version="0.1.0",
)


app.include_router(documents_router)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ai-document-intelligence-api",
    }