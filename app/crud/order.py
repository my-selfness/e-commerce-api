from models.order import OrderCreate,Order
from datetime import datetime
from bson.objectid import ObjectId
from database import cart_collection,order_collection,product_collection


def get_orders(user_id:str):
    orders=order_collection.find({"user_id":user_id})
    # {"_id":{"$oid":"66c7361f4483aaf934f2248e"},"user_id":"66bf98047b675bba5bc46e25","status":"Pending","total":{"$numberDouble":"70222.5"},"items":[{"product_id":"66be3f994cec0f2d9d78caa8","quantity":{"$numberInt":"10"}},{"product_id":"66be47f4fe66d1394551e132","quantity":{"$numberInt":"10"}}],"payment_method":"Online","shipping_address":"Mumbai","created_at":{"$date":{"$numberLong":"1724331551193"}}}

    return [Order(**{"order_id": str(order["_id"]),**order}) for order in orders]


def create_order(order_data: OrderCreate, user_id: str):
    cart = cart_collection.find_one({"user_id": user_id})
    # Cart Json
    # {'_id': ObjectId('66bfa700beb5883466915c3a'), 'user_id': '66bf98047b675bba5bc46e25', 'items': [{'product_id': '66be3f994cec0f2d9d78caa8', 'quantity': 10}, {'product_id': '66be47f4fe66d1394551e132', 'quantity': 10}]}
    result=0.0
    total=0.0
    for i in range(len(cart["items"])):
        product=product_collection.find_one({"_id":ObjectId(cart["items"][i]["product_id"])})
        # Product Json
        # {"_id":{"$oid":"66c4a662cec93e912a2e5ec4"},"name":"Speaker","price":{"$numberDouble":"1250.0"},"description":"Bass Boosted And DJ Feelings","stock":{"$numberInt":"23"}}
        if product["stock"]<cart["items"][i]["quantity"]:
            raise ValueError("Product out of stock")
        # TODO: Substract the Ordered Quantity and update the Database
        # TODO: Empty the cart
        
        qt=float(cart["items"][i]["quantity"])
        pd=float(product["price"])
        result+=qt*pd
        total+=result

    if not cart:
        raise ValueError("Cart not found")
    
    order = {
        "user_id": user_id,
        "status": "Pending",
        "total": total,
        "items": cart["items"],
        "payment_method": order_data.payment_method,
        "shipping_address": order_data.shipping_address,
        "created_at": datetime.utcnow()
    }
    result = order_collection.insert_one(order)
    return str(result.inserted_id)
