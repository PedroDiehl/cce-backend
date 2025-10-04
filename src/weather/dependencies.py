from datetime import datetime
from fastapi import HTTPException, Query


def parse_timestamp(
    timestamp: str = Query(
        ..., description="Date and time in ISO format (YYYY-MM-DDTHH:MM:SS)"
    ),
) -> datetime:
    """Dependency to parse and validate timestamp."""
    try:
        return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid timestamp. Use ISO format (YYYY-MM-DDTHH:MM:SS)",
        )
