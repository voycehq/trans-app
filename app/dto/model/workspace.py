from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class WorkspaceDTO(BaseModel):
    id: int
    name: str
    customer_id: int
    customer_count: int
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class WorkspaceDTOs(BaseModel):
    __root__: Optional[List[WorkspaceDTO]]

    class Config:
        orm_mode = True
