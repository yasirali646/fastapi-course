from typing import Optional
from fastapi import FastAPI, Body, Query, Form
 
app = FastAPI()

students = [
    {"id": 1, "name": "Yasir", "math": 90, "physics": 25, "computer": 70},
    {"id": 2, "name": "Ali", "math": 60, "physics": 45, "computer": 55},
    {"id": 3, "name": "Sara", "math": 80, "physics": 35, "computer": 65},
    {"id": 4, "name": "Aisha", "math": 50, "physics": 20, "computer": 40},
    {"id": 5, "name": "Hamza", "math": 70, "physics": 50, "computer": 60},
    {"id": 6, "name": "Noor", "math": 85, "physics": 40, "computer": 75},
    {"id": 7, "name": "Omar", "math": 55, "physics": 30, "computer": 50},
    {"id": 8, "name": "Hassan", "math": 65, "physics": 35, "computer": 60},
    {"id": 9, "name": "Zara", "math": 95, "physics": 45, "computer": 80},
    {"id": 10, "name": "Bilal", "math": 40, "physics": 25, "computer": 35}
]


@app.get("/")
def root():
    return {"message" : "Students Marksheet API"}

@app.get("/students")
def get_students(limit: Optional[int] = Query(None)):
    if limit:
        return students[:limit]
    return students


@app.post("/student")
def new_student(
    id : int = Form(),
    name: str = Form(...),
    math : int = Form(...),
    physics : int = Form(...),
    computer : int = Form(...)
):
    payload = {"id": id, "name": name, "math": math, "physics": physics, "computer": computer}
    students.append(payload)
    return {"Message": "New student has been added.", "student" : payload}


@app.get("/students/{id}")
def get_student(id: int):
    found_student = None
    for student in students:
        if student['id'] == id:
            found_student = student
            break

    if found_student is None:
        return {"Error" : "Student not found"}

    subjects = ["math", "physics", "computer"]
    total_marks = 100 * len(subjects)
    obtain_marks = 0

    for sub in subjects:
        obtain_marks += found_student[sub]
    
    percentage = round(obtain_marks / total_marks * 100, 2)
    result = "Pass" if percentage >= 40 else "Fail"

    response = {
        "Id" : found_student["id"],
        "Name" : found_student["name"],
        "Marks" : {sub: found_student[sub] for sub in subjects},
        "Total Marks" : total_marks,
        "Obtain Marks" : obtain_marks,
        "Percentage" : percentage,
        "Result": result
    }

    return response



# @app.post("/student")
# def new_student(payload: dict = Body(...)):
#     students.append(payload)
#     return {"Message": "New student has been added.", "student" : payload}


