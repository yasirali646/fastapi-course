from fastapi import FastAPI, Path, Query, HTTPException, status

from db.products import products
from routes.category import router as category_route
from routes.product import router as product_route

app = FastAPI(title="Product API")

@app.get("/")
def health():
    return { 
        "status" : "Product API is running",
        "version" : "0.1.0"
    }


app.include_router(category_route)
app.include_router(product_route)


