from datetime import datetime
from pydantic import BaseModel, Field


class LocationTime(BaseModel):

    latitude: float = Field(..., ge=-90, le=90, description="Latitude")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude")
    timestamp: datetime = Field(..., description="Date and time (ISO format)")

    class Config:
        json_schema_extra = {
            "example": {
                "latitude": 40.7128,
                "longitude": -74.0060,
                "timestamp": "2025-10-05T14:00:00",
            }
        }


class RainPrediction(BaseModel):

    will_rain: bool
    confidence: float = Field(..., ge=0, le=1)
    precipitation_probability: float = Field(..., ge=0, le=100)
    location: dict
    timestamp: datetime
    message: str
