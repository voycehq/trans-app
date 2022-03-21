from app import Base_Model


class Workspace(Base_Model):
    from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
    from sqlalchemy.orm import backref, relationship
    from datetime import datetime

    __tablename__: str = "workspace"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id", ondelete="RESTRICT"), nullable=True)
    customer_count = Column(Integer, default=0)
    default_language = Column(Integer, ForeignKey("language.id", ondelete="NO ACTION"), nullable=True)

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
                                            lazy="joined",
                                            overlaps="workspace,workspace"))