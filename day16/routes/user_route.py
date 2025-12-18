from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import get_db
from models.user_model import User
from schemas.user_schema import UserCreate, UserLogin
from auth import create_access_token

from security import get_password_hashed, verify_password
router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    user = User(
        name=new_user.name, 
        email=new_user.email, 
        password=get_password_hashed(new_user.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
    

@router.post("/login")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token(user.email)

    return {"access_token": token, "token_type": "bearer"}
