from fastapi import APIRouter

router = APIRouter(prefix="/v1/auth", tags=["Authentication"])

@router.post("/register", status_code=201)
def register():
    """Register a new user account"""
    return {"message": "TODO: implement register"}

@router.post("/login")
def login():
    """Login and receive JWT token"""
    return {"message": "TODO: implement login"}
