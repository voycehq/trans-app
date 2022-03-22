from datetime import datetime
from typing import Text, Optional, List

from pydantic import BaseModel


class TextDTO(BaseModel):
    id: int
    language_id: int
    title: str
    body: Text
    customer_id: int
    reviewed_by: Optional[int]
    workspace: Optional[int]
    date_id: int
    reviewed_date: Optional[datetime]
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class TextDTOs(BaseModel):
    __root__: Optional[List[TextDTO]]

    class Config:
        orm_mode = True
