from fastapi import APIRouter, HTTPException
from models import UserGreeting, SimpleMessage, User

router = APIRouter()

@router.get("/", response_model=SimpleMessage)
def read_root():
    return SimpleMessage(message="Hello, FastAPI!")

@router.get("/status", response_model=SimpleMessage)
def read_status():
    return SimpleMessage(message="O servidor está funcionando!")

@router.get("/user/{username}", response_model=UserGreeting)
def read_user(username: str):
    if len(username) < 3:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return UserGreeting(username=username, message=f"Welcome, {username}!")

@router.post("/create-user", response_model=User)
def create_user(user: User):
    return user