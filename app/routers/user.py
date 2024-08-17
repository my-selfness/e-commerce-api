from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from crud.user import register_user,login_for_access_token,get_current_user
from models.user import User,Token
from core.security import verify_token

auth_router=APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# user register
@auth_router.post("/register",summary="Register Users")
async def register_users(user_data: User):
    return register_user(user_data)


# user login
@auth_router.post("/token")
async def login_for_access_tokens(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    return login_for_access_token(form_data)



@auth_router.get("/profile")
async def get_current_user_endpoint(current_user: User = Depends(verify_token)):
    return get_current_user(current_user)