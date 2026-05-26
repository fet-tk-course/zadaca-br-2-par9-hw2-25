from sqlmodel import SQLModel, Field, false
from typing import Optional
from datetime import datetime
from pydantic import field_validator

class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    category: str
    duration_hours: int
    price: float
    start_date: datetime
    end_date: datetime
class CourseCreate(SQLModel):
    title: str
    category: str
    duration_hours: int
    price: float
    start_date: datetime
    end_date: datetime
    @field_validator("end_date")
    def validate_dates(cls, end_date, values):
        start_date = values.get("start_date")
        if start_date and end_date <= start_date:
            raise ValueError("end_date must be after start_date")
        return end_date
    @field_validator("duration_hours")
    def validate_duration(cls, duration_houres):
        if duration_hours <= 0:
            raise ValueError("duration_hours must be a positive number")
        return duration_hours

class CourseUpdate(SQLModel):
    title: Optional[str] = None
    category: Optional[str] = None
    duration_hours: Optional[int] = None
    price: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None