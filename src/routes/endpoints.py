from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["Endpoints"])

@router.post("/services/{service_id}/endpoints", status_code=201)
def create_endpoint(service_id: int):
    return {"message": "TODO"}

@router.get("/services/{service_id}/endpoints")
def list_endpoints(service_id: int):
    return {"message": "TODO"}

@router.get("/endpoints/{endpoint_id}")
def get_endpoint(endpoint_id: int):
    return {"message": "TODO"}

@router.put("/endpoints/{endpoint_id}")
def update_endpoint(endpoint_id: int):
    return {"message": "TODO"}