from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
def root():
    return "Hello World"


