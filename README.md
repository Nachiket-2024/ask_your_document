# Ask Your Document

---

## Overview

**Ask Your Document** is a lightweight backend microservice built with **FastAPI** and **PostgreSQL**.  
It enables users to:

- Upload documents  
- Ask questions about document content  
- Simulate an LLM-generated answer asynchronously using Python's `asyncio`

This project mimics the behavior of an LLM-powered app while focusing on core backend and async design skills.

---

## Tech Stack

- **Backend**: Python, FastAPI  
- **ORM**: SQLAlchemy  
- **Database**: PostgreSQL  
- **Async**: asyncio  
- **Dev Tools**: Uvicorn, python-dotenv, Docker 

---

## Installation (Non-Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/Nachiket-2024/ask_your_document.git
cd ask_your_document
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Rename the `.env.example` file to `.env` file at the root of the project (ask_your_document) and add the following:

```ini
# PostgreSQL Database URL (local)
DATABASE_URL=postgresql://your_user:your_password@localhost:5432/your_database

# If using Docker (connect to db container)
# DATABASE_URL=postgresql://your_user:your_password@db:5432/your_database

POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database
```

---

## Run the App

You can run the FastAPI application either locally or using Docker:

### ▶ Option 1: Run Locally (Recommended for development)

Make sure PostgreSQL is running and your `.env` is configured, then start the FastAPI app:

```bash
uvicorn backend.main:app --reload
```

### ▶ Option 2: Run with Docker (Recommended for full environment setup)

This starts both the FastAPI app and PostgreSQL in containers:

```bash
docker-compose up --build
```

---

## API Endpoints

| Method | Route                               | Description                         |
|--------|-------------------------------------|-------------------------------------|
| POST   | `/documents/`                       | Upload a document                   |
| GET    | `/documents/{document_id}`          | Get a document by ID                |
| POST   | `/documents/{document_id}/question` | Ask a question about a document     |
| GET    | `/questions/{question_id}`          | Get status and answer of a question |
| GET    | `/health`                           | Health check (returns `OK`)         |

---

## API Documentation

FastAPI automatically generates interactive API docs:

- **Swagger UI** – Try out endpoints:  
  [http://localhost:8000/docs](http://localhost:8000/docs)

- **ReDoc** – Alternative documentation UI:  
  [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Testing

You can test endpoints manually using:

- Swagger UI (`/docs`)
- curl / HTTP clients like Postman
