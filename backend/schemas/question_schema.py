# ---------------------------- External Imports ----------------------------

# Import Pydantic BaseModel and ConfigDict for schema definitions
from pydantic import BaseModel, ConfigDict

# Import datetime for the timestamp field
from datetime import datetime


# ---------------------------- Question Create Schema ----------------------------

# Schema for submitting a new question (used in POST /documents/{id}/question)
class QuestionCreate(BaseModel):
    question: str            # The user-submitted question text
    document_id: int         # The ID of the related document


# ---------------------------- Alternate Question Creation Schema ----------------------------

# Schema used when the document_id is passed via path (used in /documents/{id}/question)
class QuestionCreateTextOnly(BaseModel):
    question: str            # Only the question text is needed since document_id comes from path


# ---------------------------- Question Response Schema ----------------------------

# Schema for returning question status and answer (used in GET /questions/{id})
class QuestionResponse(BaseModel):
    id: int                             # Unique question ID
    question: str                       # The original question text
    answer: str | None = None           # The answer to the question (may be None if pending)
    status: str                         # The current status of the question: 'pending' or 'answered'
    created_at: datetime                # Timestamp when the question was created

    # Enable ORM mode to support automatic conversion from SQLAlchemy models
    class Config(ConfigDict):
        from_attributes = True
