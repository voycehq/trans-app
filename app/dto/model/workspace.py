from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field
from app.dto.model.workspace_detail import WorkspaceDetailDTO


class WorkspaceDTO(BaseModel):
    id: int
    name: str
    customer_id: int
    customer_count: int
    default_language: str
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class WorkspaceDTOs(BaseModel):
    __root__: Optional[List[WorkspaceDTO]]

    class Config:
        orm_mode = True


class CreateWorkspaceDTO(BaseModel):
    name: str = Field(..., min_length=3, max_length=20)
    default_language: str = Field(..., min_length=2)

    class Config:
        orm_mode = True
