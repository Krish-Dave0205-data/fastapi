from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Student CRUD API is running"


def test_student_crud():
    student_data = {
        "name": "Rahul Patel",
        "email": "rahul@example.com",
        "course": "B.Sc. IT",
        "semester": 5
    }

    response = client.post("/students", json=student_data)
    assert response.status_code == 201

    student = response.json()
    student_id = student["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Rahul Patel"

    response = client.get(f"/students/course")
    assert response.status_code == 200
    assert response.json()["course"] == "mca"

    response = client.get("/students")
    assert response.status_code == 200
    assert any(s["id"] == student_id for s in response.json())


    updated_data = {
        "name": "Rahul Updated",
        "email": "rahul.updated@example.com",
        "course": "B.Sc. IT",
        "semester": 6
    }

    response = client.put(
        f"/students/{student_id}",
        json=updated_data
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Rahul Updated"

    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 204

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404


def test_invalid_semester():
    response = client.post(
        "/students",
        json={
            "name": "Test Student",
            "email": "test@example.com",
            "course": "B.Sc. IT",
            "semester": 0
        }
    )
    assert response.status_code == 422