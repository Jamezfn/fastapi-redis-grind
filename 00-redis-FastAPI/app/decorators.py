from functools import wraps

def prefixed_key(func):
    """
    Decorator that prefixes returned key names with self.prefix
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        key = func(self, *args, **kwargs)
        return f"{self.prefix}:{key}"
    
    return wrapper