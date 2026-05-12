from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# TODO: Student B - Definiši svoj SQLModel entitet ovdje
# 

class Enrollment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_name: str
    student_email: str
    progress: float
    is_completed: bool = False
    date_enrolled: datetime = Field(default_factory=datetime.now)
    course_id: int = Field(foreign_key="course.id")