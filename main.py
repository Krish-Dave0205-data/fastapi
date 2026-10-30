from fastapi import FastAPI
from routes.student_routes import router

app = FastAPI(
    title="Student CRUD Application",
    description="University Student Management API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Student CRUD API is running"}