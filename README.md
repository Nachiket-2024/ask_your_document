
# Ask Your Document

---

## Overview

**Ask Your Document** is a lightweight backend microservice built with **FastAPI** and **PostgreSQL**.  
It enables users to:

- Upload documents  
- Ask questions about document content  
- Simulate an LLM-generated answer asynchronously using Python's `asyncio`

This project mimics an LLM-powered app's behavior while focusing on core backend and async design skills.

---

## Tech Stack

- **Backend**: Python, FastAPI  
- **ORM**: SQLAlchemy  
- **Database**: PostgreSQL  
- **Async**: asyncio  
- **Dev Tools**: Uvicorn, python-dotenv  

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nachiket-2024/ask_your_document.git
cd ask_your_document
```

### 2. Set up the environment

Install Backend dependencies with pip:

```bash
pip install -r requirements.txt
```

---

## .env Setup

Rename the `.env.example` file to `.env` file at the root of the project (ask_your_document) with the following content:

```ini
# Postgresql Database URL
DATABASE_URL=postgresql://username:password@localhost:5432/db_name_here

```

## Run the App

### Start the FastAPI backend

```bash
uvicorn backend.main:app --reload
```

---

### API Endpoints

| Method | Route                      | Description                         |
|--------|----------------------------|-------------------------------------|
| POST   | `/documents/`              | Upload a document                   |
| GET    | `/documents/{id}`          | Get document by ID                  |
| POST   | `/documents/{id}/question` | Ask a question about a document     |
| GET    | `/questions/{id}`          | Get status and answer of a question |
| GET    | `/health`                  | Health check (returns `OK`)         |

---

## API Documentation

FastAPI automatically provides interactive API docs.

- **Swagger UI** (Try out endpoints):  
  [http://localhost:8000/docs](http://localhost:8000/docs)

- **ReDoc** (Alternative view):  
  [http://localhost:8000/redoc](http://localhost:8000/redoc)

---
