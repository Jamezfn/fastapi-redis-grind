from pydantic import BaseModel
from typing import Optional, Any


class CacheSetRequest(BaseModel):
    """Request model for setting cache values"""
    key: str
    value: Any
    ttl: int = 300 

    class Config:
        json_schema_extra = {
            "example": {
                "key": "user:123",
                "value": {"name": "John", "role": "admin"},
                "ttl": 600
            }
        }


class CacheResponse(BaseModel):
    """Response model for cache operations"""
    key: str
    value: Any = None
    exists: bool
    ttl_remaining: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "key": "user:123",
                "value": {"name": "John", "role": "admin"},
                "exists": True,
                "ttl_remaining": 550
            }
        }


class CacheDeleteResponse(BaseModel):
    """Response model for cache deletion"""
    key: str
    deleted: bool
    message: str


class CacheStatsResponse(BaseModel):
    """Response model for cache statistics"""
    total_keys: int
    used_memory: str
    connected_clients: int
    uptime_seconds: int
    hits: int
    misses: int