from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class WorkspaceDetailDTO(BaseModel):
    id: int
    workspace_id: int
    customer_id: int
    workspace_role_id:int
    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class WorkspaceDetailDTOs(BaseModel):
    __root__: Optional[List[WorkspaceDetailDTO]]

    class Config:
        orm_mode = True
