import json
from fastapi import APIRouter
from app.core.redis_client import redis_client

router = APIRouter(prefix="/patterns", tags=["Patterns"])

@router.get("/lazy-load/{product_id}")
def lazy_load_pattern(product_id: int):
    """
    Lazy Loading Pattern Example
    """
    cached_key = f"product:{product_id}"

    cached_product = redis_client.get(cached_key)
    if cached_product:
        return {
            "pattern": "lazy_load",
            "source": "cache",
            "data": json.loads(cached_product)
        }
    
    product = {
        "id": product_id,
        "name": f"Product {product_id}",
        "price": 99.99,
        "stock": 100
    }

    redis_client.setex(cached_key, 10000, json.dumps(product))

    return {
        "pattern": "lazy_load",
        "source": "database",
        "data": product
    }

@router.get("/cache-aside/{order_id}")
def cache_aside_pattern(order_id: int):
    """
    Cache-Aside Pattern Example
    """
    cached_key = f"product:{order_id}"

    cached_product = redis_client.get(cached_key)
    if cached_product:
        return {
            "pattern": "lazy_load",
            "source": "cache",
            "data": json.loads(cached_product)
        }
    
    order = {
        "id": order_id,
        "name": f"Product {order_id}",
        "price": 99.99,
        "stock": 100
    }

    redis_client.setex(cached_key, 10000, json.dumps(order))

    return {
        "pattern": "cache_asides",
        "cached": False,
        "data": order
    }

@router.post("/cache-aside/{order_id}/update")
def update_order_cache_aside(order_id: int, status: str):
    """
    Update order and invalidate cache (Cache-Aside pattern)
    """
    cache_key = f"order:{order_id}"

    updated_order = {
        "id": order_id,
        "total": 299.99,
        "status": status,
        "items": 3
    }
    
    redis_client.delete(cache_key)

    return {
        "pattern": "cache_aside",
        "action": "update_and_invalidate",
        "cache_invalidated": True,
        "data": updated_order
    }