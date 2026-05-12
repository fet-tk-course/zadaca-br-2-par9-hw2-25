from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Enrollment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_name: str
    student_email: str
    progress: float
    is_completed: bool = False
    date_enrolled: datetime = Field(default_factory=datetime.now)
    course_id: int = Field(foreign_key="course.id")


class EnrollmentCreate(SQLModel):
    student_name: str
    student_email: str
    progress: float
    course_id: int

class EnrollmentUpdate(SQLModel):
    student_name: Optional[str] = None
    student_email: Optional[str] = None
    progress: Optional[float] = None
    is_completed: Optional[bool] = None
    course_id: Optional[int] = None