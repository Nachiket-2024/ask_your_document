# ---------------------------- External Imports ----------------------------

# Import APIRouter to define API route grouping
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


# ---------------------------- Internal Imports ----------------------------

# Import database session dependency
from ..db.session import get_db

# Import Question model
from ..models.question_model import Question

# Import schema for response
from ..schemas.question_schema import QuestionResponse

# Import logger
from ..logging.logging_config import get_logger

# Initialize logger
logger = get_logger(__name__)


# ---------------------------- Router Setup ----------------------------

router = APIRouter(prefix="/questions", tags=["Questions"])


# ---------------------------- Route: Get Question Status & Answer ----------------------------

@router.get("/{question_id}", response_model=QuestionResponse)
def get_question_status(
    question_id: int,
    db: Session = Depends(get_db)
):
    # Fetch the question by ID
    question = db.query(Question).filter(Question.id == question_id).first()

    # If question is not found, raise 404
    if not question:
        logger.error(f"Question with ID {question_id} not found.")
        raise HTTPException(status_code=404, detail="Question not found")

    # Log successful fetch
    logger.info(f"Fetched status for question ID {question_id}: status={question.status}")

    # Return the question including its status and answer
    return question
