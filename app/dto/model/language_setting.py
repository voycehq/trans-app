from datetime import datetime
from typing import Optional, Any, List

from pydantic import BaseModel


class LanguageSettingDTO(BaseModel):
    id: int
    date_id: int
    language_id: int
    details: Any
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class LanguageSettingDTOs(BaseModel):
    __root__: Optional[List[LanguageSettingDTO]]

    class Config:
        orm_mode = True
