from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime

from app import Base_Model


class WorkspaceDetail(Base_Model):

    __tablename__: str = "workspace_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)

    workspace_id = Column(Integer, ForeignKey("workspace.id", ondelete="CASCADE"), nullable=True)
    customer_id = Column(Integer, ForeignKey("customer.id", ondelete="RESTRICT"), nullable=True)
    workspace_role_id = Column(Integer, ForeignKey("workspace_role.id", ondelete="RESTRICT"), nullable=True)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)
