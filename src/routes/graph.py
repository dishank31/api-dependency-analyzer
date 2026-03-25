from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["Dependency Graph"])

@router.get("/graph/{service_id}")
def get_dependency_graph(service_id: int, depth: int = 3, direction: str = "downstream"):
    return {"message": "TODO"}

@router.get("/dependencies")
def list_dependencies(
    caller_service_id: int = None,
    callee_endpoint_id: int = None,
    page: int = 1,
    limit: int = 50
):
    return {"message": "TODO"}