# ---------------------------- External Imports ----------------------------

# Import SQLAlchemy components for ORM modeling
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func

# Import the base class for all ORM models
from ..db.base import Base


# ---------------------------- Question Model ----------------------------

# Define the Question model to store questions related to uploaded documents
class Question(Base):
    __tablename__ = "questions"  # Table name in the database

    # Unique ID for each question (Primary Key)
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to link the question to a specific document
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)

    # The actual question asked by the user
    question = Column(String, nullable=False)

    # The generated answer to the question (can be null while processing)
    answer = Column(Text, nullable=True)

    # Status of the question: "pending" (default) or "answered"
    status = Column(String, nullable=False, default="pending")

    # Timestamp for when the question was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())
