from app import Base_Model


class LanguageSetting(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Float
    from sqlalchemy.dialects.mysql import JSON

    __tablename__: str = "language_setting"

    id = Column(Integer, primary_key=True, autoincrement=True)

    language_id = Column(Integer, nullable=False)
    voice_language_name = Column(String(50), nullable=False)
    voice_language_code = Column(String(50), nullable=False)
    voice_name = Column(String(50), nullable=False)
    audio_encoding = Column(Integer, default=2)
    audio_pitch = Column(Float, default=0.00)
    audio_speaking_rate = Column(Float, default=1.00)
    details = Column(JSON, nullable=True)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)
