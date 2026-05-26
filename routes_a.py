from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_session
from models_a import Course, CourseCreate, CourseUpdate


router = APIRouter(prefix="/resursi_a", tags=["Resurs A"])

@router.post("/", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate, session: Session = Depends(get_session)):
    
    existing_course = session.exec(select(Course).where(Course.title == course.title)).first()
    if existing_course:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Course with this title already exists")
    
    existing_course1 = session.exec(select(Course).where(Course.price > 1000)).first() 
    if existing_course1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Course with price greater than 1000 is not allowed")
    
    new_course = Course.from_orm(course)
    session.add(new_course)
    session.commit()
    session.refresh(new_course)
    return new_course

@router.post("/search", response_model=Course)
def search_courses(title: str, session: Session = Depends(get_session)):
    courses = session.exec(select(Course).where(Course.title == title)).all()
    return courses

@router.get("/")
def read_courses(session: Session = Depends(get_session)):
    courses = session.exec(select(Course)).all()
    return courses

@router.get("/statistika")
def get_course_statistics(session: Session = Depends(get_session)):
    average_price = session.exec(select(Course.price)).all()
    average_price = sum(average_price) / len(average_price) if average_price else 0
    return {"average_price": average_price}

@router.get("/{id}")
def read_course(id: int, session: Session = Depends(get_session)):
    course = session.get(Course, id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course



@router.put("/{id}")
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

@router.patch("/{id}")
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

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id: int, session: Session = Depends(get_session)):    
    course = session.get(Course, id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    session.delete(course)
    session.commit()
    return None