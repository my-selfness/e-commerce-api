from fastapi import APIRouter,HTTPException,Depends
from crud.order import create_order,get_orders,order_detailed
from models.order import OrderCreate,Order
from models.user import User
from typing import Annotated
from core.utils import get_user_id


order_router=APIRouter(
    prefix="/order",
    tags=["Order"]
)
@order_router.get("/")
def get_order(user_id: Annotated[str, Depends(get_user_id)]):
    return get_orders(user_id)




@order_router.post("/", response_model=dict)
def place_order(order_data: OrderCreate, user_id: Annotated[str, Depends(get_user_id)]):
    try:
        return create_order(order_data, user_id) 
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@order_router.get("/{order_id}")
def order_details(order_id:str):
    return order_detailed(order_id)