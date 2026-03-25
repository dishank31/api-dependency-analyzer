from fastapi import APIRouter

router = APIRouter(prefix="/v1/ingest", tags=["Log Ingestion"])

@router.post("/logs", status_code=202)
def ingest_logs():
    """Receive API call logs and build dependency graph"""
    return {"message": "TODO"}