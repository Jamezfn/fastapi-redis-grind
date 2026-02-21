from fastapi import APIRouter, Depends, BackgroundTasks
import httpx

from app.deps import get_keys, get_redis
from app.keys import Keys
from app.config import settings
from app.services.timeseries import persist, calculate_three_hours_of_data
from app.services.cache import get_cache, set_cache
 
router = APIRouter()

@router.post("/refresh")
async def refresh(background_task: BackgroundTasks, redis=Depends(get_redis), keys=Depends(get_keys)):
    """
    Refresh Bitcoin sentiment data from external API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.sentiment_api_url)
        response.raise_for_status()
        data = response.json()

    await persist(redis=redis, keys=keys, data=data)

    stats = await calculate_three_hours_of_data(redis, keys)

    background_task.add_task(set_cache, redis, keys, stats)

    return stats


@router.get("/is-bitcoin-lit")
async def bitcoin(background_tasks: BackgroundTasks, redis = Depends(get_redis), keys: Keys = Depends(get_keys),):
    """
    Check if Bitcoin is "lit" based on sentiment and price trends.
    """
    cached = await get_cache(redis, keys)

    if cached:
        return cached

    stats = await calculate_three_hours_of_data(redis, keys)

    background_tasks.add_task(set_cache, redis, keys, stats)

    return stats