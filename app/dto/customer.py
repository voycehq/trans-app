from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class CustomerDTO(BaseModel):
    id: int
    full_name: str
    email: str
    password: str
    default_language: Optional[int]
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
