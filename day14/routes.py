from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import get_db
from models import Post, User
from schemas import BlogPostCreate, UserCreate, BlogPostRead, UserOut

router = APIRouter()

@router.get("/posts", response_model=list[BlogPostRead])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

@router.post("/posts/post")
def create_post(new_post: BlogPostCreate, db: Session = Depends(get_db)):
    post = Post(title=new_post.title, content=new_post.content, author_id=new_post.author_id)

    try:
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
    except IntegrityError:
        raise HTTPException(
            detail="Author doesn't exist.",
            status_code=status.HTTP_404_NOT_FOUND
        )

    except Exception:
        raise HTTPException(
            detail="Something went wrong.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    
   

    
@router.get("/users", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/users/user")
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    user = User(name=new_user.name, email=new_user.email, password=new_user.password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
    

