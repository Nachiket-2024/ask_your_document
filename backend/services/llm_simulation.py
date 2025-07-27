# ---------------------------- External Imports ----------------------------

# Import asyncio to simulate asynchronous delay
import asyncio

# ---------------------------- Internal Imports ----------------------------

# Import the Question ORM model
from ..models.question_model import Question

# Import logger utility to record events
from ..logging.logging_config import get_logger

# Initialize module-level logger
logger = get_logger(__name__)


# ---------------------------- LLM Simulation Task ----------------------------

# Define an asynchronous function to simulate background answer generation
async def simulate_llm_answer(question_id: int, db_session_factory):
    # Log the start of the simulation
    logger.info(f"Starting simulated LLM answer generation for question_id={question_id}")

    # Pause for 5 seconds to simulate LLM processing delay
    await asyncio.sleep(5)

    # Instantiate a new database session from the session factory
    db = db_session_factory()
    try:
        # Query the question entry using the provided ID
        question = db.query(Question).filter(Question.id == question_id).first()

        # If the question exists, update it with a dummy answer and mark it as answered
        if question:
            question.answer = f"This is a generated answer to your question: '{question.question}'"
            question.status = "answered"
            db.commit()  # Commit changes to the database

            # Log the successful answer generation
            logger.info(f"Answer generated and saved for question_id={question_id}")
        else:
            # Log a warning if the question is not found
            logger.warning(f"Question with ID {question_id} not found in database.")
    except Exception as e:
        # Log any unexpected exceptions
        logger.exception(f"Error during answer simulation for question_id={question_id}: {str(e)}")
    finally:
        # Always close the database session after use
        db.close()
