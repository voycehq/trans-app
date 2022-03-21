from sqlalchemy.orm import Session

from app.models.workspace_role import WorkspaceRole
from app.dto.model.workspace_role import WorkspaceRoleDTO, WorkspaceRoleDTOs


class WorkspaceRoleLib:
    """WorkspaceRoleLib for getting workspace role info from the database

    Args:
        No Args

    Usage:
        WorkspaceRoleLib().run()
    """
    from app.utils.session import session_hook

    def __init__(self):
        self.roles = ["admin", "reviewer"]

    def run(self):
        for role in self.roles:
            WorkspaceRoleLib.create(data={"name": role})

    @staticmethod
    @session_hook
    def create(db: Session, data: dict):
        workspace_role = WorkspaceRole(**data)

        db.add(workspace_role)
        db.flush()

        return WorkspaceRoleDTO.from_orm(workspace_role)

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        record = db.query(WorkspaceRole).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return WorkspaceRoleDTOs.from_orm(record).__root__ if get_all else WorkspaceRoleDTO.from_orm(record)
