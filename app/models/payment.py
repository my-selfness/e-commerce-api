from pydantic import BaseModel



class PaymentRequest(BaseModel):
    order_id: str
    payment_method: str
    amount: float

