from fastapi import HTTPException, status
from datetime import datetime, timedelta
from database import user_collection
from core.security import hash_password,authenticate_user,create_access_token
from models.user import User
from config import ACCESS_TOKEN_EXPIRE_MINUTES

def register_user(user_data: User):
    if user_collection.find_one({"email": user_data.email}):
        return {"message": "User already exists"}
    hashed_password = hash_password(user_data.password)
    user_doc = {
        "name": user_data.name,
        "email": user_data.email,
        "password": hashed_password,
        "created_at": user_data.created_at
    }
    user_collection.insert_one(user_doc)
    return {"message": "User registered successfully"}


def login_for_access_token(form_data):
    user = authenticate_user(user_collection, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(current_user: User):
    return current_user