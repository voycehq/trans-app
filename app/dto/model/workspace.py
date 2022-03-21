from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class WorkspaceDTO(BaseModel):
    from app.dto.model.workspace_detail import WorkspaceDetailDTOs
    id: int
    name: str
    customer_id: int
    customer_count: int
    default_language: int
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    workspace_detail: Optional[WorkspaceDetailDTOs]

    class Config:
        orm_mode = True


class WorkspaceDTOs(BaseModel):
    __root__: Optional[List[WorkspaceDTO]]

    class Config:
        orm_mode = True

