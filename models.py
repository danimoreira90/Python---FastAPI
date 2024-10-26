from pydantic import BaseModel, constr, conint
from datetime import date

class UserGreeting(BaseModel):
    username: str
    message: str

class SimpleMessage(BaseModel):
    message: str

class User(BaseModel):
    username: constr(min_length=1)
    age: conint(gt=0)

class Item(BaseModel):
    name: str
    description: str
    price: float

class BirthdayInfo(BaseModel):
    name: constr(min_length=1)
    birthday: date