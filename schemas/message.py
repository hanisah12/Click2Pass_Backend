from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MessageCreate(BaseModel):
    user_id: int
    name: str
    email: str
    subject: str
    message: str


class MessageUpdate(BaseModel):
    subject: str
    message: str


class MessageResponse(BaseModel):
    message_id: int
    user_id: int
    name: str
    email: str
    subject: str
    message: str