from functools import wraps
import json

from app.core.redis_client import redis_client

def cache_result(ttl=300):
    """Cache function results with specified TTL (default 5 minutes)"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{args}:{kwargs}"

            cached = redis_client.get(cache_key)
            if cached:
                return json.loads(cached)
            
            result = func(*args, **kwargs)
            redis_client.setex(cache_key, ttl, json.dumps(result))
            return result
        
        return wrapper
    
    return decorator