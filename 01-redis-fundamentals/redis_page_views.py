from fastapi import FastAPI
import redis.asyncio as redis
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = await redis.from_url(
        "redis://localhost:6379/0",
        decode_responses=True
    )
    print("Redis connection opened (lifespan startup)")

    yield

    print("Closing Redis connection (lifespan shutdown)")

app = FastAPI(lifespan=lifespan)

@app.get("/view/{path:path}")
async def record_view(path: str):
    if not path.startswith("/"):
        path = "/" + path

    key = f"pv:{path}"
    count = await app.state.redis.incr(key)

    if count == 1:
        await app.state.redis.expire(key, 14 * 24 * 3600)

    return {"path": path, "views": count}

@app.get("/health")
async def health():
    try:
        await app.state.redis.ping()
        return {"status": "healthy", "redis": "connected"}
    except Exception:
        return {"status": "unhealthy", "redis": "disconnected"}