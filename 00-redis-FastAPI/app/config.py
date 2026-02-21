from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    """Configuration class"""
    redis_url: str = Field(
        default="redis://localhost:6379",
        alias="REDIS_URL"
    )

    key_prefix: str = Field(
        default="is-bitcoin-lit",
        alias="DEFAULT_KEY_PREFIX"
    )

    sentiment_api_url: str = Field(
        default="https://api.senticrypt.com/v1/bitcoin.json",
        alias="SENTIMENT_API_URL"
    )

    hourly_bucket: str = Field(
        default="3600000",
        alias="HOURLY_BUCKET"
    )

    cache_ttl: str = Field(
        default=120,
        alias="CACHE_TTL"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()