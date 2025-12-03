from fastapi import APIRouter

from db import products

router = APIRouter(tags=["Category"])

@router.get("/categories")
def get_categories():
    categories = []
    for product in products:
        categories.append(product["category"])
    
    categories = list(set(categories))
    return categories