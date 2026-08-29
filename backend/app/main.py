from fastapi import FastAPI

app = FastAPI(
    title="AI Document Intelligence API",
    description="AI-powered document analysis and question answering platform",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ai-document-intelligence-api",
    }