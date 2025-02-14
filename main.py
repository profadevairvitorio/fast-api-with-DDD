from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from infrastructure.database import SessionLocal, engine, Base
from application.schemas import StudentCreate, StudentResponse, LessonCreate, LessonResponse
from application.crud import create_student, get_students, get_student, update_student, delete_student, create_lesson, get_lessons_by_student

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=StudentResponse)
def create_new_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)

@app.get("/students/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db)

@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_existing_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    updated_student = update_student(db, student_id, student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{student_id}")
def delete_existing_student(student_id: int, db: Session = Depends(get_db)):
    success = delete_student(db, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

@app.post("/lessons/", response_model=LessonResponse)
def create_new_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    return create_lesson(db, lesson)

@app.get("/students/{student_id}/lessons", response_model=list[LessonResponse])
def read_lessons_for_student(student_id: int, db: Session = Depends(get_db)):
    lessons = get_lessons_by_student(db, student_id)
    if not lessons:
        raise HTTPException(status_code=404, detail="No lessons found for this student")
    return lessons
