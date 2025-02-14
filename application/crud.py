from sqlalchemy.orm import Session
from domain.models import Student, Lesson
from application.schemas import StudentCreate, LessonCreate
from infrastructure.repositories import StudentRepository, LessonRepository

def create_student(db: Session, student: StudentCreate):
    student_data = Student(
        name=student.name,
        email=student.email,
        languages=",".join(student.languages),
        city=student.city,
        state=student.state
    )
    return StudentRepository.create(db, student_data)

def get_students(db: Session):
    return StudentRepository.get_all(db)

def get_student(db: Session, student_id: int):
    return StudentRepository.get_by_id(db, student_id)

def update_student(db: Session, student_id: int, student: StudentCreate):
    db_student = StudentRepository.get_by_id(db, student_id)
    if not db_student:
        return None
    db_student.name = student.name
    db_student.email = student.email
    db_student.languages = ",".join(student.languages)
    db_student.city = student.city
    db_student.state = student.state
    return StudentRepository.update(db, db_student)

def delete_student(db: Session, student_id: int):
    db_student = StudentRepository.get_by_id(db, student_id)
    if not db_student:
        return False
    StudentRepository.delete(db, db_student)
    return True

def create_lesson(db: Session, lesson: LessonCreate):
    lesson_data = Lesson(
        student_id=lesson.student_id,
        date=lesson.date,
        topic=lesson.topic,
        notes=lesson.notes
    )
    return LessonRepository.create(db, lesson_data)

def get_lessons_by_student(db: Session, student_id: int):
    return LessonRepository.get_by_student(db, student_id)
