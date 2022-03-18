from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class WorkspaceRoleDTO(BaseModel):
    id: int
    name: str
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class WorkspaceRoleDTOs(BaseModel):
    __root__: Optional[List[WorkspaceRoleDTO]]

    class Config:
        orm_mode = True
