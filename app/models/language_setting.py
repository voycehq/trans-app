from app import Base_Model


class LanguageSetting(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, DateTime, ForeignKey
    from sqlalchemy.dialects.mysql import JSON

    __tablename__: str = "language_setting"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_id = Column(Integer, ForeignKey("date.id", ondelete="RESTRICT"), nullable=False)

    language_id = Column(Integer, nullable=False)
    details = Column(JSON, nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)
