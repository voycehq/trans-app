from pydantic import Field
from pydantic.main import BaseModel


class OneToManyDTO(BaseModel):
    raw_text_id: int
    workspace_id: int
    raw_text: str = Field(..., max_length=5000)
    raw_text_language_id: int
    translation_text_id: int
    translation_text: str = Field(..., max_length=5000)
    translation_text_language_id: int

    class Config:
        orm_mode = True
