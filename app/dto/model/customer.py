from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class CustomerDTO(BaseModel):
    id: int
    full_name: str
    email: str
    password: str
    is_verified: bool
    date_id: int
    api_key: Optional[str]
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class CustomerDTOs(BaseModel):
    __root__: Optional[List[CustomerDTO]]

    class Config:
        orm_mode = True
