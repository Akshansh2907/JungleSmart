from pydantic import BaseModel
from typing import List, Optional
from src.models import Store

class Item(BaseModel):
    name: str
    quantity: int
    price: float
    hsn_code: str = "40141010"  # Default HSN code for condoms

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    items: List[Item]

class UserSignup(BaseModel):
    full_name: str
    username: str
    contact_no: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str 
    contact_no: str
    email: str
    store: Optional["Store"]

class StoreCreate(BaseModel):
    name: str
    address: str
    owner_id: int
