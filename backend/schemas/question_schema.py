# ---------------------------- External Imports ----------------------------

# Import Pydantic BaseModel and ConfigDict for schema definitions
from pydantic import BaseModel, ConfigDict

# Import datetime for the timestamp field
from datetime import datetime


# ---------------------------- Question Create Schema ----------------------------

# Schema for submitting a new question (used in POST /documents/{id}/question)
class QuestionCreate(BaseModel):
    question: str  # The user-submitted question text


# ---------------------------- Question Response Schema ----------------------------

# Schema for returning question status and answer (used in GET /questions/{id})
class QuestionResponse(BaseModel):
    id: int  # Unique question ID
    question: str  # The original question text
    answer: str | None = None  # The answer (can be None while pending)
    status: str  # The current status: 'pending' or 'answered'
    created_at: datetime  # Timestamp of question creation

    # Enable ORM mode to support conversion from SQLAlchemy models
    class Config(ConfigDict):
        from_attributes = True
