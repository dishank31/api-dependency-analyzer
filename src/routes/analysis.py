from fastapi import APIRouter

router = APIRouter(prefix="/v1/analyze", tags=["Analysis"])

@router.post("/change")
def analyze_change():
    """Analyze proposed API change for breaking impacts"""
    return {"message": "TODO"}
