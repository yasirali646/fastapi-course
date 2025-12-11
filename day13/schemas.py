from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class BlogPostBase(BaseModel):
    title: str = Field(max_length=200)
    content: str
    author: str = Field(max_length=100)


class BlogPostCreate(BlogPostBase):
    pass

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None


class BlogPost(BlogPostBase):
    id: str
    created_at: datetime

    class Config:
        from_attribute = True