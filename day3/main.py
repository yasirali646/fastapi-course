from fastapi import FastAPI, Path 

app = FastAPI()

students = [
    "Ali", "Ahmed", "Hassan", "Hussain", "Omar",
    "Zain", "Faizan", "Saad", "Shahzaib", "Hamza",
    "Bilal", "Kashif", "Asad", "Salman", "Imran",
    "Rizwan", "Usman", "Noman", "Junaid", "Rehan",
    "Ayesha", "Fatima", "Zainab", "Maria", "Hira",
    "Sana", "Iqra", "Maham", "Laiba", "Mariam",
    "Anum", "Khadija", "Hafsa", "Areeba", "Mehwish",
    "Zoya", "Amna", "Rabia", "Nida", "Aiman"
]


@app.get("/")
def root():
    return {"Message" : "hello world"}


@app.get("/filter-students")
def filter_students(sw: str,):
    filtered_names = []
    sw = sw.casefold()
    for student in students:
        if student.casefold().startswith(sw):
            filtered_names.append(student)
    return filtered_names


@app.get("/students")
def get_students():
    return students

@app.get("/students/ali")
def get_students():
    return "ali"

@app.get("/students/{id}")
def get_student(id: int = Path(ge=0, lt=len(students))):
    return students[id]








