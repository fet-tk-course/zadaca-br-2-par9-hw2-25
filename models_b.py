from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from pydantic import field_validator

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
    @field_validator("progress")
    def validate_progress(cls, progress):
        if not (0 <= progress <= 100):
            raise ValueError("progress must be between 0 and 100")
        return progress
    @field_validator("student_name")
    def validate_student_name(cls, student_name):
        if len(student_name) == 0:
            raise ValueError("student_name cannot be empty")
        return student_name

class EnrollmentUpdate(SQLModel):
    student_name: Optional[str] = None
    student_email: Optional[str] = None
    progress: Optional[float] = None
    is_completed: Optional[bool] = None
    course_id: Optional[int] = None