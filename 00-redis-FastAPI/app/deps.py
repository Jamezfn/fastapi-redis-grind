from starlette.requests import Request

from app.keys import Keys

def get_redis(request: Request):
    """Dependency to get Redis client.
    """
    return request.app.state.redis

def get_keys() -> Keys:
    """Dependency to create Keys instance.
    """
    return Keys()