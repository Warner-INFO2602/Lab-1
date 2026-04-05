from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students(pref=None):
    if pref:
        fillterd_students=[]
        for student in data:
            if student['pref'] == pref:
                fillterd_students.append(student)
        return fillterd_students
    return data

@app.get('/students/{id}')
async def get_student(id):
    for student in data:
        if student['id'] == id:
            return student
    return "Student not Found"

@app.get('/stats')
def stats():
    student_stat = {}
    student_stat['total_students'] = len(data)
    for student in data:
        if student['pref'] in student_stat:
            student_stat[student['pref']] += 1
        else:
            student_stat[student['pref']] = 1

        if student['programme'] in student_stat:
            student_stat[student['programme']] += 1
        else:
            student_stat[student['programme']] = 1

    return student_stat

@app.get('/add/{a}/{b}')
def add(a,b):
    return {'result':int(a)+int(b)}

@app.get('/subtract/{a}/{b}')
def subtract(a,b):
    return {'result':int(a)-int(b)}

@app.get('/multiply/{a}/{b}')
def multiply(a,b):
    return {'result':int(a)*int(b)}

@app.get('/divide/{a}/{b}')
def divide(a,b):
    return {'result':int(a)/int(b)}