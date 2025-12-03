from typing import Optional
from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name : str = Field(min_length=5, alias="user_name")
    age: Optional[int] = None
    address: Address



user1 = User(user_name="Ali Hyder")
user2 = User(name="Ali Mehdi", age=20, address={
    "city": "Lahore",
    "country" : "Pakistan"    
})

# print(user2.__dict__)
print(user2.model_dump())