from sqlalchemy.orm import Session
from domain.models import Student, Lesson

class StudentRepository:
    @staticmethod
    def create(db: Session, student: Student):
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    @staticmethod
    def get_all(db: Session):
        return db.query(Student).all()

    @staticmethod
    def get_by_id(db: Session, student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()

    @staticmethod
    def update(db: Session, student: Student):
        db.commit()
        db.refresh(student)
        return student

    @staticmethod
    def delete(db: Session, student: Student):
        db.delete(student)
        db.commit()


class LessonRepository:
    @staticmethod
    def create(db: Session, lesson: Lesson):
        db.add(lesson)
        db.commit()
        db.refresh(lesson)
        return lesson

    @staticmethod
    def get_by_student(db: Session, student_id: int):
        return db.query(Lesson).filter(Lesson.student_id == student_id).all()
