import uuid
from fastapi import Depends
from .security import verify_token

def convert_id(product: dict) -> dict:
    product["_id"] = str(product.pop("_id"))
    return product





def generate_uuid():
    return str(uuid.uuid4())


def is_strong_password(password: str) -> bool:
    '''
        Return True If password is strong else False.
        Use Uppercase , Lowercase , Digits , Special Characters For a Strong Password.
    '''
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in "!@#$%^&*()_+-=[]{}|;':,.<>?/" for char in password):
        return False
    return True


def format_price(price: float) -> str:
    '''
        Return Formatted Price String. Ex: ₹ 1,23,456.78
    '''
    return f"₹ {price:,.2f}"


async def get_user_id(user: dict = Depends(verify_token)):
    return user["_id"]