import time

from app.core.redis_client import redis_client

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def compute_fibonaccie_cached(n: int) -> dict:
    """Compute fibonacci with Redis caching"""
    if n > 40:
        raise ValueError("Number too large (max 40)")
    
    cached_key = f"fib:{n}"

    cached = redis_client.get(cached_key)
    if cached:
        return {
            "number": n,
            "result": int(cached),
            "cached": True,
            "message": "Retrieved from cache"
        }
    
    start_time = time.time()
    result = fibonacci(n)
    compute_time = time.time() - start_time

    redis_client.setex(cached_key, 600, str(result))

    return {
        "number": n,
        "result": result,
        "cached": False,
        "compute_time": f"{compute_time:.4f}s",
        "message": "Computed and cached for 10 minutes"
    }