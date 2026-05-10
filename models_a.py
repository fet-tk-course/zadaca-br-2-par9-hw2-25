from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Enrollment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_name: str
    progress_percentage: float
    completed: bool = False
    enrollment_date: datetime
    course_id: int


class EnrollmentCreate(SQLModel):
    student_name: str
    progress_percentage: float
    completed: bool = False
    enrollment_date: datetime
    course_id: int


class EnrollmentUpdate(SQLModel):
    student_name: Optional[str] = None
    progress_percentage: Optional[float] = None
    completed: Optional[bool] = None
    enrollment_date: Optional[datetime] = None
    course_id: Optional[int] = None


