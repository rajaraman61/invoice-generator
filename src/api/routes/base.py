from fastapi import APIRouter, HTTPException
from loguru import logger
from models.health import HealthResponse
from services.health_check import HealthHandler as health
router = APIRouter()

@router.get(
    "/", response_model=HealthResponse, name="health:get-data",
)
async def home():
    if (health.check_health()):
        return HealthResponse(True)
    else:
        return HealthResponse(False)

