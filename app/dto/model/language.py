from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class LanguageDTO(BaseModel):
    id: int
    date_id: int
    name: str
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class LanguageDTOs(BaseModel):
    __root__: Optional[List[LanguageDTO]]

    class Config:
        orm_mode = True
