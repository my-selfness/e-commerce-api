from pydantic import BaseModel,Field,EmailStr
from datetime import datetime




class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    name: str
    email: EmailStr
    password:str
    created_at: datetime = Field(default_factory=datetime.now)

class UserCreate(User):
    id: str = Field(alias='_id')

    class Config:
        orm_mode=True