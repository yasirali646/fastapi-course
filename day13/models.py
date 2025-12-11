from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    author = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())