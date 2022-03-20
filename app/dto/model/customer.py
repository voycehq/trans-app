from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List


class CustomerDTO(BaseModel):
    id: int
    full_name: str
    email: str
    password: str
    is_verified: bool
    date_id: int
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class CustomerDTOs(BaseModel):
    __root__: Optional[List[CustomerDTO]]

    class Config:
        orm_mode = True


class SignupDTO(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=20)
    email: str = Field(...)
    password: str = Field(..., min_length=8)

    class Config:
        orm_mode = True


class EmailVerificationDTO(BaseModel):
    code: str
    email: str

    class Config:
        orm_mode = True
