from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_session
from models_a import Course, CourseCreate, CourseUpdate


router = APIRouter(prefix="/resursi_a", tags=["Resurs A"])

@router.post("/resursi_a", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate, session: Session = Depends(get_session)):
    new_course = Course.from_orm(course)
    session.add(new_course)
    session.commit()
    session.refresh(new_course)
    return new_course

@router.get("/resursi_a")
def read_courses(session: Session = Depends(get_session)):
    courses = session.exec(select(Course)).all()
    return courses

@router.get("/resursi_a/{id}")
def read_course(id: int, session: Session = Depends(get_session)):
    course = session.get(Course, id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course

@router.put("/resursi_a/{id}")
def update_course(id: int, course_update: CourseUpdate, session: Session = Depends(get_session)):
    course = session.get(Course, id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    course_data = course_update.dict(exclude_unset=True)
    for key, value in course_data.items():
        setattr(course, key, value)
    
    session.add(course)
    session.commit()
    session.refresh(course)
    return course

@router.patch("/resursi_a/{id}")
def partial_update_course(id: int, course_update: CourseUpdate, session: Session = Depends  (get_session)):
    course = session.get(Course, id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    course_data = course_update.dict(exclude_unset=True)
    for key, value in course_data.items():
        setattr(course, key, value)
    
    session.add(course)
    session.commit()
    session.refresh(course)
    return course

@router.delete("/resursi_a/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id: int, session: Session = Depends(get_session)):    
    course = session.get(Course, id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    session.delete(course)
    session.commit()
    return None