from sqlalchemy.orm import Session

from app.models.workspace_role import WorkspaceRole
from app.dto.model.workspace_role import WorkspaceRoleDTO, WorkspaceRoleDTOs


class WorkspaceRoleLib:
    """WorkspaceRoleLib for getting workspace role info into the database

    Args:
        No Args

    Usage:
        WorkspaceRoleLib().run()
    """
    from app.utils.session import session_hook

    @staticmethod
    @session_hook
    def bulk_create(db: Session, names: []):
        from sqlalchemy.exc import IntegrityError

        list_to_be_updated: list = []

        for name in names:
            record:  dict = {"name": name}

            try:
                db.bulk_insert_mappings(WorkspaceRole, [record])
            except IntegrityError:
                db.rollback()
                data = db.query(WorkspaceRole).filter_by(name=record.get("name")).first()
                for key, value in record.items():
                    data.__setattr__(key, value)

                list_to_be_updated.append(WorkspaceRoleDTO.from_orm(data))

        if list_to_be_updated:
            db.bulk_update_mappings(WorkspaceRole, list_to_be_updated)

        db.flush()

        return

    @staticmethod
    @session_hook
    def find_by(db: Session, where: dict, get_all: bool = False):
        record = db.query(WorkspaceRole).filter_by(**where)
        record = record.all() if get_all else record.first()

        if not record:
            return None

        return WorkspaceRoleDTOs.from_orm(record).__root__ if get_all else WorkspaceRoleDTO.from_orm(record)

    @staticmethod
    @session_hook
    def update(db: Session, data: dict) -> WorkspaceRoleDTO:

        record = db.query(WorkspaceRole).filter_by(name=data.get("name")).first()
        for key, value in data.items():
            record.__setattr__(key, value)
        db.flush()
        return WorkspaceRoleDTO.from_orm(record)
