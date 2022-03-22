from datetime import datetime
from typing import Optional, Any, List

from pydantic import BaseModel


class LanguageSettingDTO(BaseModel):
    id: int
    
    language_id: int
    voice_language_name: str
    voice_language_code: str
    voice_name: str
    audio_encoding: int
    audio_pitch: float
    audio_speaking_rate: float
    details: Optional[Any]
    
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class LanguageSettingDTOs(BaseModel):
    __root__: Optional[List[LanguageSettingDTO]]

    class Config:
        orm_mode = True
