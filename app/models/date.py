from app import Base_Model


class Date(Base_Model):
    from datetime import datetime
    from sqlalchemy import Column, Integer, String, DateTime, Boolean

    __tablename__: str = "date"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_date= Column(DateTime, nullable=False)
    date_full_name = Column(String(100), nullable=False)
    date_key = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    is_leap_year = Column(Boolean, default=False)
    month_number = Column(Integer, nullable=False)
    month_name = Column(String(100), nullable=False)
    year_week = Column(Integer, nullable=False)
    day_of_week = Column(Integer, nullable=False)
    day_of_month = Column(Integer, nullable=False)
    day_of_year = Column(Integer, nullable=False)
    day_name = Column(String(100), nullable=False)
    is_working_day = Column(Boolean, nullable=False)
    quarter = Column(Integer, nullable=False)
    Year_half = Column(Integer, nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, onupdate=datetime.utcnow())
    deleted_on = Column(DateTime, nullable=True)

