from app import Base_Model


class Customer(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

    __tablename__: str = "customer"

    id = Column(Integer, primary_key=True, autoincrement=True)

    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    api_key = Column(String(255), nullable=True)

    is_verified = Column(Boolean, default=False)
    date_id = Column(Integer, ForeignKey("date.id", ondelete="RESTRICT"), nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)


