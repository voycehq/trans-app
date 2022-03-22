from pydantic import Field
from pydantic.main import BaseModel


class OneToOneDTO(BaseModel):
    workspace_id: int
    raw_text: str = Field(..., max_length=5000)
    raw_text_language_id: int
    translation_text_language_id: int

    class Config:
        orm_mode = True
