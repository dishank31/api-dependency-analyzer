from fastapi import APIRouter

router = APIRouter(prefix="/v1/services", tags=["Services"])

@router.post("/", status_code=201)
def create_service():
    return {"message": "TODO"}

@router.get("/")
def list_services():
    return {"message": "TODO"}

@router.get("/{service_id}")
def get_service(service_id: int):
    return {"message": "TODO", "service_id": service_id}

@router.put("/{service_id}")
def update_service(service_id: int):
    return {"message": "TODO"}

@router.delete("/{service_id}", status_code=204)
def delete_service(service_id: int):
    return None