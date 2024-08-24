from fastapi import APIRouter,Depends
from typing import Annotated 
from models.payment import PaymentRequest
from core.utils import get_user_id
from crud.payment import get_payment


payment_router=APIRouter(prefix="/payment",tags=["Payments"])


@payment_router.post('/')
def get_payments_details(payment_request:PaymentRequest,user_id:Annotated[str, Depends(get_user_id)]):
    return payment_request