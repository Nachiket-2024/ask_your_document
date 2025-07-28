# ---------------------------- External Imports ----------------------------

# Import APIRouter for creating API route groups
from fastapi import APIRouter, Depends, HTTPException, status, Path, UploadFile, File

# Import SQLAlchemy Session for database operations
from sqlalchemy.orm import Session

# Import asyncio for background tasks
import asyncio

# Import os for creating directories and handling file paths
import os

# Import shutil to write uploaded file contents to disk
import shutil


# ---------------------------- Internal Imports ----------------------------

# Import database session dependency
from ..db.session import get_db, SessionLocal

# Import Document model for interacting with the documents table
from ..models.document_model import Document

# Import Question model for question table operations
from ..models.question_model import Question

# Import response schema for documents
from ..schemas.document_schema import DocumentResponse

# Import schemas related to question creation/response
from ..schemas.question_schema import QuestionCreateTextOnly, QuestionResponse

# Import mock LLM service for async question answering
from ..services.llm_simulation import simulate_llm_answer

# Import logger utility
from ..logging.logging_config import get_logger

# Initialize module-level logger
logger = get_logger(__name__)


# ---------------------------- Router Setup ----------------------------

# Create a router for all document-related endpoints
router = APIRouter(prefix="/documents", tags=["Documents"])


# ---------------------------- Route: Upload and Create Document ----------------------------

# Define a POST endpoint that accepts only file upload to create a document
@router.post("/", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def create_document_from_file(
    # UploadFile object extracted from form-data file input
    file: UploadFile = File(...),
    # Inject database session
    db: Session = Depends(get_db)
):
    # Define a base directory for uploaded files
    upload_dir = "project_uploads"

    # Create the directory if it does not exist
    os.makedirs(upload_dir, exist_ok=True)

    # Generate the complete path where file will be saved
    file_path = os.path.join(upload_dir, file.filename)

    # Save uploaded file content to the file path on disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Prepare dummy content that includes the file name
    dummy_content = f"this is the content {file.filename}"

    # Create a new Document instance using filename and dummy content
    new_doc = Document(
        title=file.filename,
        content=dummy_content
    )

    # Add the document to the session for DB insertion
    db.add(new_doc)

    # Commit the transaction to persist the document
    db.commit()

    # Refresh the document object to populate auto-generated fields like ID
    db.refresh(new_doc)

    # Log the creation of the new document
    logger.info(f"Document created from upload: ID={new_doc.id}, filename={file.filename}")

    # Return the created document as response
    return new_doc


# ---------------------------- Route: Get Document by ID ----------------------------

# Define a GET endpoint to retrieve a document by its ID
@router.get("/{document_id}", response_model=DocumentResponse)
async def get_document(document_id: int, db: Session = Depends(get_db)):
    # Query the database for the document with the given ID
    document = db.query(Document).filter(Document.id == document_id).first()

    # If the document is not found, log error and raise a 404 Not Found error
    if not document:
        logger.error(f"Document with ID {document_id} not found")
        raise HTTPException(status_code=404, detail="Document not found")

    # Log document retrieval
    logger.info(f"Document retrieved with ID {document_id}")

    # Return the found document as the response
    return document


# ---------------------------- Route: Ask Question for Document ----------------------------

# Define a POST endpoint to ask a question about a specific document
@router.post("/{document_id}/question", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
async def ask_question_for_document(
    # Path parameter to identify the target document
    document_id: int = Path(...),
    # Request body containing the question text
    q: QuestionCreateTextOnly = ...,
    # Injected database session
    db: Session = Depends(get_db)
):
    # Query the database to ensure the document exists
    document = db.query(Document).filter(Document.id == document_id).first()

    # If the document is not found, log error and raise a 404 Not Found error
    if not document:
        logger.error(f"Document with ID {document_id} not found while asking question")
        raise HTTPException(status_code=404, detail="Document not found")

    # Create a new Question instance with "pending" status
    question = Question(
        document_id=document_id,
        question=q.question,
        status="pending"
    )

    # Add the question to the DB session
    db.add(question)

    # Commit the session to save the question
    db.commit()

    # Refresh the question instance to access its ID
    db.refresh(question)

    # Start an asynchronous background task to simulate answering the question
    asyncio.create_task(simulate_llm_answer(question.id, db_session_factory=SessionLocal))

    # Log successful question creation
    logger.info(f"Question submitted with ID {question.id} for document ID {document_id}")

    # Return the question object immediately; the answer will be processed in the background
    return question
