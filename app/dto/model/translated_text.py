from datetime import datetime
from typing import Text, Optional, List

from pydantic import BaseModel


class TranslatedTextDTO(BaseModel):
    id: int
    text_id: int
    language_id: int
    body: Text
    reviewed_by: int
    reviewed_date: Optional[datetime]
    translated_date: datetime
    audio_generation_date: datetime
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class TranslatedTextDTOs(BaseModel):
    __root__: Optional[List[TranslatedTextDTO]]

    class Config:
        orm_mode = True
