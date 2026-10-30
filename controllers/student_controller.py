from fastapi import HTTPException
from models.student_model import StudentCreate, StudentUpdate


students = {}


next_id = 1


def create_student(student: StudentCreate):
    global next_id

    student_data = {
        "id": next_id,
        **student.model_dump()
    }

    students[next_id] = student_data
    next_id += 1

    return student_data


def get_all_students():
    return list(students.values())


def get_student_by_id(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


# 4. Update Student
def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student_data = {
        "id": student_id,
        **student.model_dump()
    }

    students[student_id] = student_data

    return student_data


# 5. Delete Student
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]

    return None