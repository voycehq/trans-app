from app import Base_Model


class Verification(Base_Model):
    from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
    from datetime import datetime

    __tablename__: str = "verification"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customer.id", ondelete="CASCADE"), nullable=True)
    verification_type = Column(String(255), nullable=False)
    code = Column(String(255), nullable=True)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)