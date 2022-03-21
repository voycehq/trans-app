from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class VerificationDTO(BaseModel):

    id: int
    customer_id: int
    verification_type: str
    code: Optional[str]
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class VerificationDTOs(BaseModel):
    __root__: Optional[List[VerificationDTO]]

    class Config:
        orm_mode = True
