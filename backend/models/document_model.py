# ---------------------------- External Imports ----------------------------

# Import SQLAlchemy components for ORM modeling
from sqlalchemy import Column, Integer, String, Text

# Import the base class for all ORM models
from ..db.base import Base


# ---------------------------- Document Model ----------------------------

# Define the Document model to store uploaded document information
class Document(Base):
    __tablename__ = "documents"  # Table name in the database

    # Unique ID for each document (Primary Key)
    id = Column(Integer, primary_key=True, index=True)

    # Title of the document
    title = Column(String, nullable=False)

    # Full text content of the document
    content = Column(Text, nullable=False)
