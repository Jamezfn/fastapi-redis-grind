from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

from app.redis_client import create_redis
from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown"""
    app.state.redis = await create_redis(settings.redis_url)
    await app.state.redis.ping()
    logger.info('Redis connected')
    yield
    await app.state.redis.aclose()

app = FastAPI(title="Bitcoin Sentiment API", lifespan=lifespan)