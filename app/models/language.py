from app import Base_Model
from app.dto.model.language import LanguageDTO


class Language(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
    from typing import Optional

    from app.utils.connection import SessionLocal
    from app.utils.session import session_hook

    __tablename__: str = "language"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_id = Column(Integer, ForeignKey("date.id", ondelete="RESTRICT"), nullable=False)

    name = Column(String(150), nullable=False)
    code = Column(String(2), nullable=False)
    html_code = Column(String(50), nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)

    @staticmethod
    @session_hook
    def get_by_code(db: SessionLocal, code: str) -> Optional[LanguageDTO]:
        language = db.query(Language).filter(Language.code == code).first()
        
        return LanguageDTO.from_orm(language) if language else None
