# Ask Your Document

---

## Overview

ask_your_document is a lightweight backend microservice built with FastAPI and PostgreSQL. It lets users upload documents and ask questions about their content. Answers are simulated asynchronously using Python's asyncio, mimicking the behavior of a language model without actual LLM integration.

---

## Tech Stack

- **Backend**: Python ,FastAPI, SQLAlchemy, PostgreSQL 

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

## Run the App

### Start the FastAPI backend

```bash
uvicorn backend.main:app --reload
```

---

## .env Setup

Make a `.env` file at the root of the project (ask_your_document) with the following content:

```ini
# Postgresql Database URL
DATABASE_URL=postgresql://username:password@localhost:5432/db_name_here

```

---
