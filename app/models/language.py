from app import Base_Model

class Language(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

    __tablename__: str = "language"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(150), nullable=False)
    code = Column(String(2), nullable=False)
    html_code = Column(String(50), nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)
