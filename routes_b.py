from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_session
from models_b import Enrollment, EnrollmentCreate, EnrollmentUpdate
from typing import Optional, List

router = APIRouter(prefix="/resursi_b", tags=["Resurs B"])


@router.post("/", response_model=Enrollment, status_code=status.HTTP_201_CREATED)
def create_enrollment(enrollment: EnrollmentCreate, session: Session = Depends(get_session)):
    db_enrollment = Enrollment.model_validate(enrollment)
    session.add(db_enrollment)
    session.commit()
    session.refresh(db_enrollment)
    return db_enrollment

@router.get("/", response_model=List[Enrollment])
def read_enrollments(student_name: Optional[str] = None, session: Session = Depends(get_session)):
    statement = select(Enrollment)
    if student_name:
        statement = statement.where(Enrollment.student_name == student_name)
    
    results = session.exec(statement).all()
    return results


@router.get("/{id}", response_model=Enrollment)
def read_enrollment(id: int, session: Session = Depends(get_session)):
    enrollment = session.get(Enrollment, id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment