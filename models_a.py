from sqlmodel import SQLModel, Field, false
from typing import Optional
from datetime import datetime


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
class CourseUpdate(SQLModel):
    title: Optional[str] = None
    category: Optional[str] = None
    duration_hours: Optional[int] = None
    price: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None