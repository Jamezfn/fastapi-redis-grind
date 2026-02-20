from fastapi import APIRouter, Depends, BackgroundTasks
import httpx

from app.deps import get_keys, get_redis
from app.keys import Keys
from app.config import settings
 
router = APIRouter()

@router.post("/refresh")
async def refresh(backround_task: BackgroundTasks, redis=Depends(get_redis), keys=Depends(get_keys)):
    """
    Refresh Bitcoin sentiment data from external API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.sentiment_api_url)
        response.raise_for_status()
        data = response.json()
    return data

@router.get("/mock/sentiment")
async def mock_sentiment():
    return {"sentiment": "positive", "score": 0.85}