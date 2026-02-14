from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.redis_client import test_connection
from app.routes import users, compute, cache

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown events"""
    test_connection()
    yield

app = FastAPI(
    title="Simple Cache API",
    description="Redis Caching with FastAPI",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(users.router)
app.include_router(compute.router)
app.include_router(cache.router)