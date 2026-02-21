import json
from datetime import datetime

from app.keys import Keys
from app.config import settings
from app.utils.utils import datetime_parser


async def get_cache(redis, keys: Keys):
    cached = await redis.get(keys.cache_key())

    if not cached:
        return None

    return json.loads(cached, object_hook=datetime_parser)


async def set_cache(redis, keys: Keys, data):
    def serialize_dates(v):
        return v.isoformat() if isinstance(v, datetime) else v

    await redis.set(
        keys.cache_key(),
        json.dumps(data, default=serialize_dates),
        ex=settings.cache_ttl,
    )