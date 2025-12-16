from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

class BogPostOut(BaseModel):
    title: str = Field(max_length=200)
    content: str
    created_at: datetime

    class config:
        from_attribute = True

class UserOut(UserBase):
    id: int
    posts: list[BogPostOut] = []


    class config:
        from_attribute = True

