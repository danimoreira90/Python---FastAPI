from pydantic import BaseModel

class UserGreeting(BaseModel):
    username: str
    message: str
