from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import get_db
from models.post_model import Post
from schemas.post_schema import BlogPostCreate, BlogPostRead

router = APIRouter(prefix="/posts")

@router.get("/", response_model=list[BlogPostRead])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

@router.post("/post")
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

    
   
