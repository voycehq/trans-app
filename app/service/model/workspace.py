from sqlalchemy.orm import Session

from app.dto.model.workspace import WorkspaceDTO, WorkspaceDTOs
from app.models.workspace import Workspace
from app.dto.model.workspace_detail import WorkspaceDetailDTO


class WorkspaceLib:
    from app.utils.session import session_hook

    @staticmethod
    @session_hook
    def create(db: Session, data: dict):
        workspace = Workspace(**data)

        db.add(workspace)
        db.flush()

        return WorkspaceDTO.from_orm(workspace)

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        record = db.query(Workspace).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return WorkspaceDTOs.from_orm(record).__root__ if get_all else WorkspaceDTO.from_orm(record)

    @staticmethod
    @session_hook
    def update(db: Session, data: dict) -> WorkspaceDTO:

        record = db.query(Workspace).filter_by(name=data.get("name"),
                                               customer_id=data.get("customer_id")).first()

        for key, value in data.items():
            record.__setattr__(key, value)
        db.flush()
        return WorkspaceDTO.from_orm(record)
