from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from infrastructure.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    languages = Column(String, nullable=False)  # Armazenado como string separada por vírgulas
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)

    lessons = relationship("Lesson", back_populates="student")

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    date = Column(Date, nullable=False)
    topic = Column(String, nullable=False)
    notes = Column(String, nullable=True)

    student = relationship("Student", back_populates="lessons")
