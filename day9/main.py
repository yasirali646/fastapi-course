from fastapi import FastAPI, status, Path, HTTPException
from fastapi.responses import JSONResponse
import uuid

from models import UserCreate, User

app = FastAPI(title="FastAPI with Pydantic")

users = [
    User(id="1", name="Ali", age=25),
    User(id="2", name="Imran", age=35),
    User(id="3", name="Yaseen", age=41),
]

@app.get("/")
def root():
    return { "message" : "Server is running", "status" : "200"}


@app.get("/users")
def get_users():
    return users


@app.post("/user")
def add_user(user: UserCreate):
    new_id = uuid.uuid4().hex[:8]

    new_user = User(id=new_id, **user.model_dump())

    return JSONResponse(
        content=new_user.model_dump(),
        status_code=status.HTTP_201_CREATED
    )

@app.get("/users/{id}")
def get_user(id: str = Path(...)):

    found_user = None
    for user in users:
        if user.id == id:
            found_user = user
    
    if found_user is None:
        raise HTTPException(
            detail="User not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return JSONResponse(
        content=found_user.model_dump(),
        status_code=status.HTTP_200_OK
    )