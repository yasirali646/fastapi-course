from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

