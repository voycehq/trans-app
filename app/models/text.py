from app import Base_Model

class OriginalText(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
    from sqlalchemy.orm import relationship, backref

    __tablename__: str = "text"

    id = Column(Integer, primary_key=True, autoincrement=True)

    language_id = Column(Integer, ForeignKey("language.id", ondelete="RESTRICT"), nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.id", ondelete="NO ACTION"), nullable=False)
    reviewed_by = Column(Integer, ForeignKey("customer.id", ondelete="NO ACTION"), nullable=True)
    workspace = Column(Integer, ForeignKey("workspace.id", ondelete="CASCADE"), nullable=True)
    date_id = Column(Integer, ForeignKey("date.id", ondelete="RESTRICT"), nullable=False)
    reviewed_date = Column(DateTime, nullable=True)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)

    translated_text = relationship("TranslatedText",
                                    backref=backref("translated_text",
                                                    lazy="joined"))
