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

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    phone: str=Field(min_length=10, max_length=10)
  
class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=10, max_length=10)
    password: Optional[str] = None
