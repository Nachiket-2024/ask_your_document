# Use a minimal Python 3.13.5 image based on Debian Bookworm (slim variant)
FROM python:3.13.5-slim-bookworm

# Set the working directory inside the container to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends gcc libffi-dev libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies list
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy Alembic config into /app
COPY alembic.ini .

# Copy Alembic migration scripts (the folder) into /app
COPY alembic/ alembic/

# Copy backend source code
COPY ./backend/ ./backend/

# Expose FastAPI port
EXPOSE 8000

# Set PYTHONPATH for internal imports
ENV PYTHONPATH=/app

# Run Uvicorn server (can be overridden by docker-compose)
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
