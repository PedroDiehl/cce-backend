from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = "CCE Rain Prediction API"
    DESCRIPTION: str = "API to check if it will rain at a specific location and time"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
