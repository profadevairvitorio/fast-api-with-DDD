from pydantic import BaseModel
from typing import List
from datetime import date

class StudentCreate(BaseModel):
    name: str
    email: str
    languages: List[str]
    city: str
    state: str

class StudentResponse(StudentCreate):
    id: int

    class Config:
        orm_mode = True

class LessonCreate(BaseModel):
    student_id: int
    date: date
    topic: str
    notes: str

class LessonResponse(LessonCreate):
    id: int

    class Config:
        orm_mode = True
