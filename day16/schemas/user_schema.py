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

class UserRead(BaseModel):
    name: str
    email: str

    class config:
        from_attribute = True

class UserLogin(BaseModel):
    email: str
    password: str