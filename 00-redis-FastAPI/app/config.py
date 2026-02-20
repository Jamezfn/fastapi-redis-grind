from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Configuration class"""
    redis_url: str = Field(
        default="redis://localhost:6379",
        alias="REDIS_URL"
    )

settings = Settings()