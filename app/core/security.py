from passlib.context import CryptContext  
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import  Depends, HTTPException, status
from database import user_collection
from jose import JWTError, jwt
from config import ACCESS_TOKEN_EXPIRE_MINUTES,SECRET_KEY,ALGORITHM
from models.user import User




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




def authenticate_user(user_collection, email: str, password: str):
    user = user_collection.find_one({"email": email})
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        user =user_collection.find_one({"email": decoded_token.get("sub")})
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        user["_id"] = str(user["_id"])  
        return {
            "_id": user["_id"],
            "name": user["name"],
            "email": user["email"],
            "created_at": user["created_at"]
        }
        # return User(**user) 
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    