import uvicorn
from fastapi import FastAPI
from settings import settings
from weather.router import router as weather_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    debug=settings.DEBUG,
    docs_url="/api/docs",
)

app.include_router(weather_router, prefix="/api", tags=["weather"])


@app.get("/api")
def get_info():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "debug_mode": settings.DEBUG,
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG
    )
