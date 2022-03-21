from sqlalchemy.orm import Session

from app.models.workspace_detail import WorkspaceDetail
from app.dto.model.workspace_detail import WorkspaceDetailDTO,WorkspaceDetailDTOs


class WorkspaceDetailLib:
    from app.utils.session import session_hook

    @staticmethod
    @session_hook
    def create(db: Session, data: dict):
        workspace_detail = WorkspaceDetail(**data)

        db.add(workspace_detail)
        db.flush()

        return WorkspaceDetailDTO.from_orm(workspace_detail)


    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        record = db.query(WorkspaceDetail).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return WorkspaceDetailDTOs.from_orm(record).__root__ if get_all else WorkspaceDetailDTO.from_orm(record)

    @staticmethod
    @session_hook
    def update(db: Session, data: dict) -> WorkspaceDetailDTO:

        record = db.query(WorkspaceDetailDTO).filter_by(customer_id=data.get("customer_id"),
                                                          workspace_id=data.get("workspace_id")).first()
        for key, value in data.items():
            record.__setattr__(key, value)
        db.flush()

        return WorkspaceDetailDTO.from_orm(record)