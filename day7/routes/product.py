from typing import List
from fastapi import APIRouter, Query, Path, HTTPException, status
from pydantic import BaseModel

from db import products

router = APIRouter(tags=["Product"])


@router.get("/products")
def get_products():
    return products


@router.get("/products/filter")
def filter_products(
    limit: int = Query(None),
    order: str = Query("asc"),
    min_price: float = Query(0),
    max_price: float = Query(None)
):
    filtered = []

    # Price Range
    for product in products:
        if product["price"] >= min_price and (max_price is None or product["price"] <= max_price):
            filtered.append(product)

    # Product Order
    reverse_order = order.lower() == "desc"
    filtered.sort(key = lambda x: x["title"].lower(), reverse=reverse_order)

    # Limit
    if limit:
        filtered = filtered[:limit]
    

    return filtered

@router.get("/products/{slug}")
def get_product(slug: str = Path()):

    for p in products:
        if p["slug"] == slug:
            return p
    
    # return {"error" : "Product not found."}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found."
    )