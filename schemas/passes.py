from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional


class PassCreate(BaseModel):
    user_id: int
    pass_type: str
    id_proof: str=Field(min_length=12, max_length=12)
    valid_from: date
    valid_till: date


class PassUpdate(BaseModel):
    pass_type: str
    valid_from: date
    valid_till: date


class PassResponse(BaseModel):
    pass_id: int
    user_id: int
    pass_type: str
    id_proof: str=Field(min_length=12, max_length=12)
    valid_from: date
    valid_till: date
 
class PassPatch(BaseModel):
    pass_type: Optional[str] = None
    valid_from: Optional[date] = None
    valid_till: Optional[date] = None