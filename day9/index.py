from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from datetime import datetime



app = FastAPI(title="FastApi with Jinja2")
templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1,
        "title": "Understanding FastAPI",
        "content": "FastAPI is a modern web framework for building APIs with Python.",
        "author": "Yasir",
        "created_at": datetime(2025, 1, 10)
    },
    {
        "id": 2,
        "title": "What is Jinja2?",
        "content": "Jinja2 is a templating engine used to create dynamic HTML pages.",
        "author": "Ali",
        "created_at": datetime(2025, 2, 14)
    }
]

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts})