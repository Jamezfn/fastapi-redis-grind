import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def test_connection():
    """Test Redis connection"""
    try:
        redis_client.ping()
        print("✓ Connected to Redis successfully!")
        return True
    except redis.ConnectionError:
        print("✗ Failed to connect to Redis. Make sure Redis is running.")
        return False
    
def get_redis_client():
    """Get Redis client instance"""
    return redis_client