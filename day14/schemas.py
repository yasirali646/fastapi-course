from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class BlogPostBase(BaseModel):
    title: str = Field(max_length=200)
    content: str

class BlogPostCreate(BlogPostBase):
    author_id : int

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class BlogPost(BlogPostBase):
    id: int
    created_at: datetime
    author_id : int

class BogPostOut(BlogPostBase):
    created_at: datetime

    class config:
        from_attribute = True



class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

class UserRead(UserBase):
    pass

class UserOut(UserBase):
    id: int
    posts: list[BogPostOut] = []


    class config:
        from_attribute = True


class BlogPostRead(BlogPostBase):
    id: int
    author : UserRead

    class config:
        from_attribute=True


