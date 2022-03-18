from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from app import Base_Model


class Customer(Base_Model):
    __tablename__: str = "customer"

    id = Column(Integer, primary_key=True, autoincrement=True)

    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    default_language = Column(Integer, ForeignKey("language.id", ondelete="NO ACTION"), nullable=True)
    date_id = Column(Integer, ForeignKey("date.id", ondelete="RESTRICT"), nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)

    workspace = relationship("Workspace",
                             backref=backref("workspace",
                                             lazy="joined",
                                             single_parent=True,
                                             passive_deletes=True))
    workspace_detail = relationship("WorkspaceDetail",
                                    backref=backref("workspace_detail",
                                                    lazy="joined"))

    text = relationship("OriginalText",
                        backref=backref("workspace_detail",
                                                lazy="joined"))