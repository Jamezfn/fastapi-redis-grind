import redis.asyncio as redis

async def create_redis(redis_url: str) -> redis.Redis:
    """Create a redis connection"""
    return redis.from_url(redis_url, decode_responses=True)