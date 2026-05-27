from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

app = FastAPI(
    title="Student Card API",
    description="API to consult and register students",
    version="1.0.0"
)

class Student(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    program: str = Field(..., min_length=1)
    active: bool


students = [
    {
        "id": 1,
        "name": "Javier Esteban Perez Gomez",
        "email": "javierperez232@gmail.com",
        "program": "Análisis y Desarrollo de Software",
        "active": True
    },
    
    {
        "id": 2,
        "name": "Mateo Alexander Paredes García",
        "email": "mateoparedespg@outlook.com",
        "program": "Producción Multimedia",
        "active": False
    },
    
    {
        "id": 3,
        "name": "Brayan Steven Moreno Gutierrez",
        "email": "brayanmoreno4567@gmail.com",
        "program": "Producción Multimedia",
        "active": False
    },
    
    {
        "id": 4,
        "name": "Nicol Stefania Perez Manrique",
        "email": "nicolperezmanrique@gmail.com",
        "program": "Analisis y Desarrollo de Software",
        "active": True
    },
     
    {
        "id": 5,
        "name": "Edwar Mateo Perez Garcia",
        "email": "edwarperezgarcia2143@gmail.com",
        "program": "Analisis y Desarrollo de Software",
        "active": True
    }, 
]


def get_next_id() -> int:
    return max((s["id"] for s in students), default=0) + 1


@app.get("/students/{id}", response_model=dict)
def get_student(id: int) -> dict:
    for student in students:
        if student["id"] == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students", status_code=201, response_model=dict)
def create_student(student: Student) -> dict:
    new_student = student.dict()
    new_student["id"] = get_next_id()
    students.append(new_student)
    return new_student


@app.get("/students", response_model=List[dict])
def list_students(active: Optional[bool] = Query(None)) -> List[dict]:
    if active is None:
        return students
    return [s for s in students if s["active"] == active]

