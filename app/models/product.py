from pydantic import BaseModel,Field
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: float
    description: str = None
    stock: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str = Field(alias='_id')

    class Config:
        orm_mode = True
