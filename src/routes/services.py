from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.db import get_db

router = APIRouter(prefix="/v1/services", tags=["Services"])

@router.get("/")
def list_services(db: Session = Depends(get_db)):
    return {"message": "TODO"}

@router.post("/", status_code=201)
def create_service(db: Session = Depends(get_db)):
    return {"message": "TODO"}

@router.get("/{service_id}")
def get_service(service_id: int, db: Session = Depends(get_db)):
    return {"message": "TODO", "service_id": service_id}

@router.put("/{service_id}")
def update_service(service_id: int, db: Session = Depends(get_db)):
    return {"message": "TODO"}

@router.delete("/{service_id}", status_code=204)
def delete_service(service_id: int, db: Session = Depends(get_db)):
    return None