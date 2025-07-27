# ---------------------------- External Imports ----------------------------

# Import FastAPI Router
from fastapi import APIRouter

# ---------------------------- Router Setup ----------------------------

# Define the router for health check
router = APIRouter(tags=["Health"])


# ---------------------------- Route: Health Check ----------------------------

# Define a simple GET route to verify service is up
@router.get("/health")
async def health_check():
    # Return a basic health message
    return {"status": "ok"}
