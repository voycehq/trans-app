from pydantic import Field
from pydantic.main import BaseModel


class CreateWorkspaceDTO(BaseModel):
    name: str = Field(..., min_length=3)
    default_language: str = Field(..., min_length=2)

    class Config:
        orm_mode = True
