from app import Base_Model


class WorkspaceRole(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, String, DateTime

    __tablename__: str = "workspace_role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)