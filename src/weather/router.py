from datetime import datetime
from .models import RainPrediction
from .service import WeatherService
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(prefix="/weather", tags=["weather"])
weather_service = WeatherService()


@router.get("/rain/predict", response_model=RainPrediction)
async def predict_rain(
    latitude: float = Query(..., ge=-90, le=90, description="Latitude of the location"),
    longitude: float = Query(
        ..., ge=-180, le=180, description="Longitude of the location"
    ),
    timestamp: str = Query(
        ..., description="Date and time in ISO format (YYYY-MM-DDTHH:MM:SS)"
    ),
):
    try:
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid timestamp. Use ISO format (YYYY-MM-DDTHH:MM:SS)",
        )

    try:
        result = await weather_service.predict_rain(latitude, longitude, dt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
