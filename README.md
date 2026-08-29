# AI Document Intelligence

AI-powered document analysis and question-answering platform using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

## 🚧 Project Status

**In Development**

This project is being built as a production-oriented AI application to explore and demonstrate modern Generative AI application development.

## 🎯 Goals

* Upload and process documents
* Extract and intelligently search document content
* Implement Retrieval-Augmented Generation (RAG)
* Use Large Language Models for question answering
* Provide source citations for generated answers
* Build a modern React-based user interface
* Containerize the application with Docker
* Deploy the application to Azure
* Implement automated testing and CI/CD

## 🏗️ Planned Technology Stack

### Frontend

* React
* TypeScript

### Backend

* Python
* FastAPI

### AI

* Large Language Models (LLMs)
* Embeddings
* Retrieval-Augmented Generation (RAG)
* Vector Search
* LangChain / LangGraph

### Database

* PostgreSQL
* pgvector

### DevOps & Cloud

* Docker
* GitHub Actions
* Microsoft Azure

## 📁 Project Structure

```text
ai-document-intelligence/
├── backend/
│   ├── alembic/          # Database migrations
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Configuration and database
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # API schemas
│   │   ├── services/     # Business services
│   │   └── rag/          # RAG pipeline
│   ├── storage/          # Local uploaded documents (not committed)
│   └── requirements.txt
│
├── frontend/             # React application
├── docs/                 # Architecture and technical documentation
├── infrastructure/       # Docker and cloud infrastructure
├── .env.example          # Environment variable template
├── docker-compose.yml
├── .gitignore
└── README.md
```

## 🚀 Current Progress

* [x] Project repository created
* [x] Initial project structure
* [x] FastAPI backend initialized
* [x] PostgreSQL + pgvector setup
* [x] SQLAlchemy database integration
* [x] Alembic database migrations
* [x] Document and document chunk database models
* [x] PDF document upload
* [x] Local document storage
* [ ] PDF text extraction
* [ ] Document text chunking
* [ ] Embedding generation
* [ ] Vector search
* [ ] RAG pipeline
* [ ] LLM integration
* [ ] Automated testing
* [ ] React frontend
* [ ] Authentication
* [ ] Docker deployment
* [ ] Azure deployment
* [ ] CI/CD


## 👨‍💻 Author

**Dilpreet Singh Hardoi**

Full Stack & AI Developer
