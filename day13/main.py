from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from database import Base, engine
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastApi with Jinja2")
templates = Jinja2Templates(directory="templates")

app.include_router(router)
