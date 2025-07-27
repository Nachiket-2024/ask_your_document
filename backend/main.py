# ---------------------------- External Imports ----------------------------

# Load environment variables from .env file  
from dotenv import load_dotenv

# Work with file paths in an OS-independent way  
from pathlib import Path

# Import FastAPI framework  
from fastapi import FastAPI, Request

# CORS middleware for handling cross-origin requests  
from fastapi.middleware.cors import CORSMiddleware

# To send error response for global exception handling  
from fastapi.responses import JSONResponse


# ---------------------------- Environment Setup ----------------------------

# Get the base directory (3 levels up from current file)  
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from the .env file in base directory  
_ = load_dotenv(dotenv_path=BASE_DIR / ".env")


# ---------------------------- Logging Setup ----------------------------

# Custom middleware to log every API request  
from .logging.logging_middleware import LoggingMiddleware

# JSON-formatted rotating logger  
from .logging.logging_config import get_logger

# Create or reuse logger instance  
logger = get_logger("main")


# ---------------------------- Internal Imports ----------------------------

# Import the document-related routes from the API module  
from .api.document_routes import router as document_router

# Import the question-related routes from the API module  
from .api.question_routes import router as question_router

# Import the health route from the API module  
from .api.health_routes import router as health_router


# ---------------------------- App Initialization ----------------------------

# Create a FastAPI application instance  
app = FastAPI()


# ---------------------------- Middleware Configuration ----------------------------

# Add CORS middleware to allow requests from any origin (for development)  
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],               # Allow all origins (use specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],               # Allow all HTTP methods
    allow_headers=["*"],               # Allow all headers
)

# Add custom logging middleware to log all incoming requests/responses  
app.add_middleware(LoggingMiddleware)


# ---------------------------- Global Exception Handler ----------------------------

# Define a global exception handler for catching unhandled exceptions  
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Log the error with request path and message  
    logger.exception(f"Unhandled Exception at {request.url.path}: {str(exc)}")

    # Return a 500 Internal Server Error response  
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )


# ---------------------------- Router Registration ----------------------------

# Register the document routes with the FastAPI app  
app.include_router(document_router)

# Register the question routes with the FastAPI app  
app.include_router(question_router)

# Register the health route with the FastAPI app  
app.include_router(health_router)


# ---------------------------- Root Route ----------------------------

# Define a simple root route to verify the API is running  
@app.get("/")
def read_root():
    return {"message": "Welcome to the Ask Your Document App!"}
