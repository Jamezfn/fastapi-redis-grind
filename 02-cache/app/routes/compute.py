from fastapi import APIRouter, HTTPException, status

from app.services.fibonacci import compute_fibonaccie_cached

router = APIRouter(prefix="/compute", tags=["Computation"])

@router.get("/fibonacci/{n}")
def compute_fibonacci(n: int):
    """Compute fibonacci number with caching"""
    try:
        return compute_fibonaccie_cached(n)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
