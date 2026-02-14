from fastapi import APIRouter, HTTPException, status

from app.services.external_api import get_user_with_cache_info

router = APIRouter(
    prefix="/users",
    tags=["External API"]
)

@router.get("/{user_id}")
def get_user(user_id: int):
    """Get user data from external API with caching"""
    result = get_user_with_cache_info(user_id)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return result