from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class DateDTO(BaseModel):
    id: int
    full_date: datetime
    date_full_name: str
    date_key: str
    year: int
    is_leap_year: bool
    month_number: int
    month_name: str
    year_week: int
    day_of_week: int
    day_of_month:int
    day_of_year:int
    day_name: str
    is_working_day: bool
    quarter: int
    year_half: int

    created_on: datetime
    updated_on: Optional[datetime]
    deleted_on: Optional[datetime]

    class Config:
        orm_mode = True


class DateDTOs(BaseModel):
    __root__: Optional[List[DateDTO]]

    class Config:
        orm_mode = True
