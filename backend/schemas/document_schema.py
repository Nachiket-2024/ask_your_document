# ---------------------------- External Imports ----------------------------

# Import Pydantic BaseModel for defining request/response schemas
from pydantic import BaseModel, ConfigDict


# ---------------------------- Document Create Schema ----------------------------

# Schema for creating a new document (used in POST /documents/)
class DocumentCreate(BaseModel):
    title: str  # Title of the document
    content: str  # Full content of the document


# ---------------------------- Document Response Schema ----------------------------

# Schema for returning a document (used in GET /documents/{id})
class DocumentResponse(DocumentCreate):
    id: int  # Unique identifier of the document

    # Enable ORM mode to support reading from SQLAlchemy models
    class Config(ConfigDict):
        from_attributes = True
