from database import product_collection
from models.product import  ProductCreate,Product
from typing import List,Optional
from bson import ObjectId
from core.utils import convert_id




async def get_products(skip: int, limit: int) -> List[Product]:
    products = product_collection.find().skip(skip).limit(limit)
    products_list = list(products)
    products_list = [convert_id(product) for product in products_list]
    # print(products_list)
    return [Product(**product) for product in products_list]

async def get_product(product_id: str) -> Optional[Product]:
    product = product_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        product = convert_id(product)
        return Product(**product)
    return None


async def create_product(product: ProductCreate) -> Product:
    product_dict = product.dict()
    result = product_collection.insert_one(product_dict)
    product_dict["_id"] = str(result.inserted_id)
    return Product(**product_dict)




async def update_product(product_id: str, product: ProductCreate) -> Optional[Product]:
    update_result = product_collection.update_one(
        {"_id": ObjectId(product_id)}, {"$set": product.dict()}
    )
    if update_result.modified_count == 1:
        updated_product = product_collection.find_one({"_id": ObjectId(product_id)})
        if updated_product:
            return Product(**updated_product)
    return None


async def delete_product(product_id: str) -> bool:
    delete_result = product_collection.delete_one({"_id": ObjectId(product_id)})
    return delete_result.deleted_count == 1