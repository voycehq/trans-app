from app import Base_Model


class TranslatedText(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text

    __tablename__: str = "translated_text"

    id = Column(Integer, primary_key=True, autoincrement=True)

    text_id = Column(Integer, ForeignKey("text.id", ondelete="CASCADE"), nullable=False)
    language_id = Column(Integer, ForeignKey("language.id", ondelete="RESTRICT"), nullable=False)

    body = Column(Text, nullable=False)
    reviewed_by = Column(Integer, ForeignKey("customer.id", ondelete="NO ACTION"), nullable=True)
    reviewed_date = Column(DateTime, nullable=True)
    translated_date = Column(DateTime, nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)
