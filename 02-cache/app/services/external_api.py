from app.services.cache_decorator import cache_result
import time
import requests

@cache_result(ttl=120)
def fetch_user_data(user_id: int):
    """Simulate fetching user data from external API
    Uses cache decorator for automatic caching"""
    time.sleep(1)
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json() if response.status_code == 200 else None


def get_user_with_cache_info(user_id: int) -> dict:
    """Get user data with cache timing information"""
    start_time = time.time()
    user_data = fetch_user_data(user_id)
    response_time = time.time() - start_time

    is_cached = response_time < 0.5

    return {
        "data": user_data,
        "cached": is_cached,
        "response_time": f"{response_time:.4f}s"
    }