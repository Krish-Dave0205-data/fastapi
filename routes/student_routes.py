from fastapi import APIRouter, status, Response
from models.student_model import Student, StudentCreate, StudentUpdate
from controllers import student_controller

router = APIRouter()


@router.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):
    return student_controller.create_student(student)



@router.get(
    "/students",
    response_model=list[Student],
    status_code=status.HTTP_200_OK
)
def get_all_students():
    return student_controller.get_all_students()



@router.get(
    "/students/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def get_student(student_id: int):
    return student_controller.get_student_by_id(student_id)

@router.get(
    "/students/course",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def get_student():
 return student_controller.get_all_students()


@router.put(
    "/students/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def update_student(student_id: int, student: StudentUpdate):
    return student_controller.update_student(student_id, student)



@router.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):
    student_controller.delete_student(student_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)