from fastapi import APIRouter
from models import UserResponse

router = APIRouter()

@router.get("/", response_model=UserResponse)
def read_root():
    return UserResponse(message="Hello, FastAPI!")

@router.get("/status", response_model=UserResponse)
def read_status():
    return UserResponse(message="O servidor está funcionando!")

@router.get("/user/{username}", response_model=UserResponse)
def read_user(username: str):
    return UserResponse(message=f"Olá, {username}!")
