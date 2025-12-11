from fastapi import FastAPI, Request, Form, Path, HTTPException, status, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session


from schemas import BlogPost, BlogPostCreate, BlogPostUpdate
from database import get_db
from models import Post

from fastapi import APIRouter


router = APIRouter(prefix="/posts")


templates = Jinja2Templates(directory="templates")


@router.get("/")
def root(request: Request, db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})

@router.get("/create")
def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request" : request})

@router.post("/create")
def create_form(request: Request, title: str = Form(...), content: str = Form(...), author: str = Form(...), db: Session = Depends(get_db)):
  
  payload = BlogPostCreate(title=title, content=content, author=author)

  post = Post(**payload.model_dump())

  db.add(post)
  db.commit()
  db.refresh(post)
  
  return RedirectResponse(url=f"/posts/{post.id}", status_code=303)

@router.get("/{post_id}")
def post_detail(request: Request, post_id: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post:
        return templates.TemplateResponse("detail.html", {"request": request, "post": post})
    
    return templates.TemplateResponse("detail.html", {"request": request, "post": None}, status_code=404)

@router.get("/edit/{post_id}")
def edit_form(request: Request, post_id: str = Path(...), db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        return templates.TemplateResponse("edit.html", {"request": request, "post": post})
    raise HTTPException(
        detail="Post not found!",
        status_code=status.HTTP_404_NOT_FOUND
    )

@router.post("/edit/{post_id}")
def update_form(
   post_id: str = Path(...),
   title: str = Form(...), 
   content: str = Form(...), 
   author: str = Form(...),
   db: Session = Depends(get_db) 
):
    
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(
            detail="Post not found!",
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    post.title = title
    post.content = content
    post.author = author

    db.commit()
    db.refresh(post)

    return RedirectResponse(url=f"/posts/{post.id}", status_code=303)
    

@router.post("/delete/{post_id}")
def delete_post(post_id: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(
            detail="Post not found!",
            status_code=status.HTTP_404_NOT_FOUND
        )    

    db.delete(post)
    db.commit()

    return RedirectResponse(url="/posts", status_code=303)

