from pydantic import BaseModel
from pydantic import conint, constr

class UserGreeting(BaseModel):
    username: str
    message: str

class SimpleMessage(BaseModel):
    message: str

class User(BaseModel):
    username: constr(min_length=1)
    age: conint(gt=0)