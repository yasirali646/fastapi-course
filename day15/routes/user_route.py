from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import get_db
from models.post_model import Post
from models.user_model import User
from schemas.user_schema import UserCreate, UserOut

router = APIRouter(prefix="/users")


@router.get("/", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/user")
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    user = User(name=new_user.name, email=new_user.email, password=new_user.password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
    

