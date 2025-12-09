from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from models import BlogPost, BlogPostCreate, BlogPostUpdate
from fastapi.responses import RedirectResponse

from typing import List
from datetime import datetime
from uuid import UUID, uuid4


app = FastAPI(title="FastApi with Jinja2")
templates = Jinja2Templates(directory="templates")

posts : List[BlogPost] = [
    BlogPost(
        id="1",
        title="Understanding FastAPI",
        content="FastAPI is a modern web framework for building APIs with Python.",
        author="Imran Ali",
        created_at=datetime.utcnow()
    )
]

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})


@app.get("/create")
def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request" : request})


@app.get("/posts/{post_id}")
async def post_detail(request: Request, post_id: str):
    for p in posts:
        if str(p.id) == post_id:
            return templates.TemplateResponse("detail.html", {"request": request, "post": p})
    return templates.TemplateResponse("detail.html", {"request": request, "post": None}, status_code=404)

@app.post("/create")
def create_form(request: Request, title: str = Form(...), content: str = Form(...), author: str = Form(...)):
  
  payload = BlogPostCreate(title=title, content=content, author=author)

  post = BlogPost(
        id=str(len(posts) + 1),
        title=payload.title,
        content=payload.content,
        author=payload.author,
        created_at=datetime.utcnow()
    )


  posts.insert(0, post)
  return RedirectResponse(url=f"/posts/{post.id}", status_code=303)

