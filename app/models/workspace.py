from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import backref, relationship

from app import Base_Model


class Workspace(Base_Model):
    __tablename__: str = "workspace"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id", ondelete="RESTRICT"), nullable=True)
    customer_count = Column(Integer, default=0)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)

    text = relationship("OriginalText",
                        backref=backref("text",
                                        lazy="joined",
                                        cascade="delete, all",
                                        passive_deletes=True))

    workspace_detail = relationship("WorkspaceDetail",
                                    backref=backref("workspace_detail",
                                                    lazy="joined",
                                                    cascade="delete, all",
                                                    passive_deletes=True))

    customer = relationship("Customer",
                            backref=backref("customer",
                                            lazy="joined"))