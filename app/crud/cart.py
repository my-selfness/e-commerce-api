from database import cart_collection
from models.cart import CartItem,Cart



def get_cart(user_id: str):
    cart = cart_collection.find_one({"user_id": user_id})
    if cart:
        for item in cart.get("items", []):
            item["product_id"] = str(item["product_id"])
        return Cart(**cart)
    return Cart(user_id=user_id, items=[])

def add_to_cart(user_id: int, item: CartItem):
    cart=cart_collection.find_one({"items.product_id": item.product_id})
    if not cart:
        cart_collection.update_one(
            {"user_id": user_id},
            {"$push": {"items": item.dict()}},
            upsert=True
        )
        return {"message": "Item added to cart"}
    return {"message": "Item Already in the cart"}

def update_cart(user_id: str, item: CartItem):
    cart_collection.update_one(
        {"user_id": user_id, "items.product_id": item.product_id},
        {"$set": {"items.$.quantity": item.quantity}}
    )
    return {"message": "Cart updated"}


def remove_from_cart(user_id: int, product_id: int):
    cart_collection.update_one(
        {"user_id": user_id},
        {"$pull": {"items": {"product_id": product_id}}}
    )
    return {"message": "Item removed from cart"}