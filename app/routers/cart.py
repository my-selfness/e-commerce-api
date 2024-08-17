from fastapi import APIRouter,HTTPException,Depends
from crud.cart import get_cart,add_to_cart,update_cart,remove_from_cart
from models.cart import CartItem,Cart
from models.user import User
from typing import Annotated
from core.security import verify_token
from core.utils import get_user_id
cart_router=APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@cart_router.get("/", response_model=Cart)
def read_cart(user_id: Annotated[str, Depends(get_user_id)]):
    cart = get_cart(user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@cart_router.post("/", response_model=dict)
def create_cart_item(user_id: Annotated[ str , Depends(get_user_id)], item: CartItem):
    add_to_cart(user_id, item)
    return {"message": "Item added to cart"}


@cart_router.put("/", response_model=dict)
def update_cart_item(user_id: Annotated[ str , Depends(get_user_id)], item: CartItem):
    update_cart(user_id, item)
    return {"message": "Cart updated"}

@cart_router.delete("/{product_id}", response_model=dict)
def delete_cart_item(user_id: Annotated[str,Depends(get_user_id)], product_id: str):
    remove_from_cart(user_id, product_id)
    return {"message": "Item removed from cart"}