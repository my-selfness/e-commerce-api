from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: str
    name: str
    price: float
    description: Optional[str] = None
    stock: int