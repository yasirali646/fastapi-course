from fastapi import FastAPI

from models.post_model import Post
from models.user_model import User
from database import Base, engine
from routes.user_route import router as user_router
from routes.post_route import router as post_router


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(user_router)
app.include_router(post_router)

