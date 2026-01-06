from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str=Field(min_length=10, max_length=10)
    password: str

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: str=Field(min_length=10, max_length=10)
    password: str


class UserResponse(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    phone: str=Field(min_length=10, max_length=10)
  

