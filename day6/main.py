from fastapi import FastAPI, Path, Query, HTTPException, status

app = FastAPI(title="Product API")

products = [
    {"id": 1, "title": "Wireless Mouse", "slug": "wireless-mouse", "description": "Smooth and silent wireless mouse.",
     "price": 1499, "tags": ["electronics", "accessories"], "stock": 34, "category": "Electronics"},
    {"id": 2, "title": "Gaming Keyboard", "slug": "gaming-keyboard", "description": "RGB mechanical gaming keyboard.",
     "price": 6999, "tags": ["gaming", "mechanical"], "stock": 12, "category": "Electronics"},
    {"id": 3, "title": "Leather Wallet", "slug": "leather-wallet", "description": "Handmade genuine leather wallet.",
     "price": 2500, "tags": ["fashion", "accessories"], "stock": 20, "category": "Fashion"},
    {"id": 4, "title": "Bluetooth Speaker", "slug": "bluetooth-speaker",
     "description": "Portable speaker with deep bass.", "price": 3999, "tags": ["audio", "portable"], "stock": 15,
     "category": "Electronics"},
    {"id": 5, "title": "Running Shoes", "slug": "running-shoes",
     "description": "Lightweight running shoes for daily use.", "price": 5200, "tags": ["sports", "shoes"], "stock": 18,
     "category": "Sportswear"},
    {"id": 6, "title": "Cotton T-Shirt", "slug": "cotton-tshirt", "description": "Soft cotton t-shirt for casual wear.",
     "price": 999, "tags": ["clothing", "casual"], "stock": 45, "category": "Fashion"},
    {"id": 7, "title": "Stainless Steel Bottle", "slug": "steel-bottle",
     "description": "Insulated bottle keeps water cold for 12 hours.", "price": 1200, "tags": ["kitchen", "fitness"],
     "stock": 27, "category": "Home & Kitchen"},
    {"id": 8, "title": "Notebook Pack", "slug": "notebook-pack", "description": "Set of 5 ruled notebooks.",
     "price": 450, "tags": ["stationery"], "stock": 60, "category": "Stationery"},
    {"id": 9, "title": "Office Chair", "slug": "office-chair",
     "description": "Ergonomic office chair with lumbar support.", "price": 14999, "tags": ["furniture", "office"],
     "stock": 7, "category": "Furniture"},
    {"id": 10, "title": "Smartwatch", "slug": "smartwatch",
     "description": "Fitness tracking smartwatch with notifications.", "price": 8500,
     "tags": ["wearables", "electronics"], "stock": 14, "category": "Electronics"},
    {"id": 11, "title": "Scented Candles", "slug": "scented-candles", "description": "Set of 3 aromatic candles.",
     "price": 1600, "tags": ["home-decor", "aroma"], "stock": 22, "category": "Home Decor"},
    {"id": 12, "title": "Dish Rack", "slug": "dish-rack", "description": "Rust-free stainless steel dish rack.",
     "price": 2100, "tags": ["kitchen"], "stock": 13, "category": "Home & Kitchen"},
    {"id": 13, "title": "Yoga Mat", "slug": "yoga-mat", "description": "Non-slip yoga mat for workouts.", "price": 1800,
     "tags": ["fitness", "sports"], "stock": 26, "category": "Sportswear"},
    {"id": 14, "title": "Phone Tripod", "slug": "phone-tripod",
     "description": "Adjustable tripod stand for mobile phones.", "price": 1300, "tags": ["accessories", "photography"],
     "stock": 19, "category": "Electronics"},
    {"id": 15, "title": "USB-C Charger", "slug": "usb-c-charger", "description": "Fast charging USB-C wall adapter.",
     "price": 1700, "tags": ["electronics"], "stock": 30, "category": "Electronics"},
    {"id": 16, "title": "Travel Backpack", "slug": "travel-backpack",
     "description": "Water-resistant backpack for travel.", "price": 4300, "tags": ["travel", "bags"], "stock": 11,
     "category": "Travel"},
    {"id": 17, "title": "Non-stick Frying Pan", "slug": "nonstick-pan", "description": "Durable non-stick frying pan.",
     "price": 2600, "tags": ["kitchen"], "stock": 16, "category": "Home & Kitchen"},
    {"id": 18, "title": "Table Lamp", "slug": "table-lamp", "description": "Soft warm-light study lamp.", "price": 2100,
     "tags": ["lighting", "home-decor"], "stock": 10, "category": "Home Decor"},
    {"id": 19, "title": "Gaming Headset", "slug": "gaming-headset", "description": "Surround sound headset with mic.",
     "price": 5500, "tags": ["gaming", "audio"], "stock": 8, "category": "Electronics"},
    {"id": 20, "title": "Electric Kettle", "slug": "electric-kettle",
     "description": "1.5L electric kettle with auto shut-off.", "price": 3200, "tags": ["kitchen", "appliances"],
     "stock": 21, "category": "Home & Kitchen"}
]


@app.get("/")
def health():
    return { 
        "status" : "Product API is running",
        "version" : "0.1.0"
    }

@app.get("/products")
def get_products():
    return products


@app.get("/products/filter")
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

@app.get("/products/{slug}")
def get_product(slug: str = Path()):

    for p in products:
        if p["slug"] == slug:
            return p
    
    # return {"error" : "Product not found."}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found."
    )


