from fastapi import APIRouter,HTTPException
from crud.product import get_products,create_product,update_product,get_product,delete_product
from models.product import ProductCreate,Product
from typing import List


product_router=APIRouter(prefix='/products',tags=["Products"])



# Get Limited Product
@product_router.get("/",response_model=List[Product],summary="Fetch Only Limited Products")
async def read_products(skip:int=0,limit:int=10):
    '''
        Fetch Only Limited  Products
        Response = [{ "_id": "str", "name": "string", "price": "float", "description": "string", "stock": "integer" }, ... ]
    '''
    products = await get_products(skip=skip, limit=limit)
    return products


# Get Product Details by Id
@product_router.get("/{product_id}", response_model=Product,summary="Get Details of Product")
async def read_product(product_id: str):
    product = await get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Create Product
@product_router.post("/", response_model=Product,summary="Create Product")
async def create_new_product(product: ProductCreate):
    return await create_product(product)

# Update Product
@product_router.put("/{product_id}", response_model=Product,summary="Update Product")
async def update_existing_product(product_id: str, product: ProductCreate):
    '''
        Update Product by Product ID
    '''
    updated_product = await update_product(product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

# Delete the Product
@product_router.delete("/{product_id}", response_model=bool,summary="Delete The Product")
async def delete_existing_product(product_id: str):
    success = await delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return success