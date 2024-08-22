from pydantic import BaseModel,Field
from typing import List

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderCreate(BaseModel):
    cart_id: str | None = None
    payment_method: str
    shipping_address: str

class Order(BaseModel):
    order_id: str 
    status: str
    total: float
    items: List[OrderItem]

    class Config:
        orm_mode = True
