from fastapi import APIRouter, HTTPException, Path
from models import UserGreeting, SimpleMessage, User, Item, BirthdayInfo
from typing import Dict
from utils import calculate_days_until_birthday

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

items: Dict[int, Item] = {
    1: Item(name="Tesla Model S", description="Battery-electric, four-door full-size car that has been produced by the American automaker Tesla since 2012.", price=242000),
    2: Item(name="Bugatti Chiron", description="Mid-engine two-seater sports car designed in Germany by Bugatti Engineering GmbH[7] and manufactured in France, by French automobile manufacturer Bugatti Automobiles S.A.S. ", price=10000000)
}

@router.get("/item/{item_id}", response_model=Item)
def get_item(item_id: int = Path(..., description="The ID of the item to retrieve")):
    if item_id in items:
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/item/{item_id}", response_model=dict)
def delete_item(item_id: int = Path(..., description="The ID of the item to delete")):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/birthday")
def get_birthday_message(birthday_info: BirthdayInfo):
    days_until_birthday = calculate_days_until_birthday(birthday_info.birthday)
    return {"message": f"Hello {birthday_info.name}, there are {days_until_birthday} days until your next birthday!"}