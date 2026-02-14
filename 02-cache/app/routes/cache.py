import json
from fastapi import APIRouter, HTTPException, status

from app.core.redis_client import redis_client
from app.models.cache_models import (
    CacheSetRequest,
    CacheResponse,
    CacheDeleteResponse,
    CacheStatsResponse
)

router = APIRouter(prefix="/cache", tags=["Cache Management"])

@router.post("/set")
def set_cache(request: CacheSetRequest):
    """
    Manually set a cache value
    """
    redis_client.setex(request.key, request.ttl, json.dumps(request.value))
    return {
        "message": "Cache set successfully",
        "key": request.key,
        "ttl": request.ttl
    }

@router.get("/get/{key}", response_model=CacheResponse)
def get_cache(key: str):
    """
    Get a cached value
    """
    value = redis_client.get(key)

    if value is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "key": key,
                "value": None,
                "exists": False
            }
        )
    
    ttl = redis_client.ttl(key)

    return {
        "key": key,
        "value": json.loads(value),
        "exists": True,
        "ttl_remaining": ttl
    }

@router.delete("/delete/{key}", response_model=CacheDeleteResponse)
def delete_cache(key: str):
    """
    Delete a cache entry
    """
    deleted = redis_client.delete(key)
    return {
        "key": key,
        "deleted": bool(deleted),
        "message": "Deleted successfully" if deleted else "Key not found"
    }


@router.get("/stats", response_model=CacheStatsResponse)
def cache_stats():
    """
    Get Redis cache statistics
    """
    info = redis_client.info()
    keys_count = redis_client.dbsize()
    
    return {
        "total_keys": keys_count,
        "used_memory": info.get('used_memory_human', 'N/A'),
        "connected_clients": info.get('connected_clients', 0),
        "uptime_seconds": info.get('uptime_in_seconds', 0),
        "hits": info.get('keyspace_hits', 0),
        "misses": info.get('keyspace_misses', 0)
    }


@router.post("/flush")
def flush_cache():
    """
    Clear all cache (use with caution!)
    """
    redis_client.flushdb()
    return {"message": "All cache cleared"}