from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    course: str = Field(min_length=1)
    marks: int = Field(ge=1)


class Student(StudentCreate):
    id: int


class StudentUpdate(StudentCreate):
    pass