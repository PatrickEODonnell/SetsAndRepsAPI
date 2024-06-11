from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

exercises = [{"Id": 1, "Name":"Barbell Bench Press","Difficulty":"Intermediate","Primary":"Pectorals"},
{"Id": 1, "Name":"Dumbbell Bench Press","Difficulty":"Intermediate","Primary":"Pectorals"},
{"Id": 2, "Name":"Incline Dumbbell Press","Difficulty":"Intermediate","Primary":"Upper Pectorals"},
{"Id": 3, "Name":"Decline Dumbbell Press","Difficulty":"Intermediate","Primary":"Lower Pectorals"},
{"Id": 4, "Name":"Push-Ups","Difficulty":"Beginner","Primary":"Pectorals"},
{"Id": 5, "Name":"Cable Flyes","Difficulty":"Intermediate","Primary":"Pectorals"},
{"Id": 6, "Name":"Pull-Ups","Difficulty":"Advanced","Primary":"Latissimus Dorsi"},
{"Id": 7, "Name":"Barbell Rows","Difficulty":"Intermediate","Primary":"Latissimus Dorsi"},
{"Id": 8, "Name":"Seated Cable Rows","Difficulty":"Intermediate","Primary":"Latissimus Dorsi"},
{"Id": 9, "Name":"Lat Pulldown","Difficulty":"Intermediate","Primary":"Latissimus Dorsi"},
{"Id": 10, "Name":"Dumbbell Rows","Difficulty":"Intermediate","Primary":"Latissimus Dorsi"},
{"Id": 11, "Name":"Face Pulls","Difficulty":"Intermediate","Primary":"Rotator Cuff (Shoulders)"},
{"Id": 12, "Name":"Military Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 13, "Name":"Lateral Raises","Difficulty":"Intermediate","Primary":"Medial Deltoids (Sides of Shoulders)"},
{"Id": 14, "Name":"Front Raises","Difficulty":"Beginner","Primary":"Anterior Deltoids (Front of Shoulders)"},
{"Id": 15, "Name":"Arnold Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 16, "Name":"Reverse Flyes","Difficulty":"Intermediate","Primary":"Posterior Deltoids (Rear of Shoulders)"},
{"Id": 17, "Name":"Upright Rows","Difficulty":"Intermediate","Primary":"Trapezius"},
{"Id": 18, "Name":"Barbell Curls","Difficulty":"Beginner","Primary":"Biceps"},
{"Id": 19, "Name":"Dumbbell Curls","Difficulty":"Beginner","Primary":"Biceps"},
{"Id": 20, "Name":"Hammer Curls","Difficulty":"Beginner","Primary":"Brachialis (Outer Forearm)"},
{"Id": 21, "Name":"Concentration Curls","Difficulty":"Intermediate","Primary":"Biceps"},
{"Id": 22, "Name":"Preacher Curls","Difficulty":"Intermediate","Primary":"Biceps Triceps"},
{"Id": 23, "Name":"Pushdowns","Difficulty":"Beginner","Primary":"Triceps"},
{"Id": 24, "Name":"Overhead Triceps Extensions","Difficulty":"Intermediate","Primary":"Triceps"},
{"Id": 25, "Name":"Lying Triceps Extensions","Difficulty":"Intermediate","Primary":"Triceps"},
{"Id": 26, "Name":"Dips","Difficulty":"Intermediate","Primary":"Triceps"},
{"Id": 27, "Name":"Close-Grip Bench Press","Difficulty":"Intermediate","Primary":"Triceps"},
{"Id": 28, "Name":"Dumbbell Shoulder Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 29, "Name":"Landmine Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 30, "Name":"Seated Arnold Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 31, "Name":"Peck Deck Flyes","Difficulty":"Beginner","Primary":"Pectorals"},
{"Id": 32, "Name":"Cable Chest Press","Difficulty":"Intermediate","Primary":"Pectorals"},
{"Id": 33, "Name":"Incline Dumbbell Flyes","Difficulty":"Intermediate","Primary":"Upper Pectorals"},
{"Id": 34, "Name":"Decline Cable Flyes","Difficulty":"Intermediate","Primary":"Lower Pectorals"},
{"Id": 35, "Name":"Seated Cable Rows (Neutral Grip)","Difficulty":"Intermediate","Primary":"Latissimus Dorsi"},
{"Id": 36, "Name":"Inverted Rows","Difficulty":"Intermediate","Primary":"Latissimus Dorsi"},
{"Id": 37, "Name":"Seated Cable Face Pulls","Difficulty":"Intermediate","Primary":"Rotator Cuff (Shoulders)"},
{"Id": 38, "Name":"Standing Barbell Overhead Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 39, "Name":"Seated Dumbbell Arnold Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 40, "Name":"Dumbbell Bicep Curls (Hammer Grip)","Difficulty":"Beginner","Primary":"Brachialis (Outer Forearm)"},
{"Id": 41, "Name":"Seated Ez-Bar Curls","Difficulty":"Intermediate","Primary":"Biceps"},
{"Id": 42, "Name":"Skullcrushers","Difficulty":"Intermediate","Primary":"Triceps"},
{"Id": 43, "Name":"Overhead Dumbbell Triceps Extensions","Difficulty":"Intermediate","Primary":"Triceps"},
{"Id": 44, "Name":"Kneeling Cable Tricep Pushdowns","Difficulty":"Intermediate","Primary":"Triceps"},
{"Id": 45, "Name":"Diamond Push-Ups","Difficulty":"Intermediate","Primary":"Triceps"},
{"Id": 46, "Name":"Kneeling Single-Arm Arnold Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 47, "Name":"Dumbbell Lunges with Overhead Press","Difficulty":"Intermediate","Primary":"Shoulders"},
{"Id": 48, "Name":"Dumbbell Chest Flyes on Swiss Ball","Difficulty":"Intermediate","Primary":"Pectorals"},
{"Id": 49, "Name":"Single-Arm Cable Row","Difficulty":"Intermediate","Primary":"Latissimus Dorsi"},
{"Id": 50, "Name":"Kneeling Single-Arm Cable Curl","Difficulty":"Intermediate","Primary":"Biceps"},
{"Id": 51, "Name":"Cable Woodchoppers","Difficulty":"Intermediate","Primary":"Obliques"},
{"Id": 52, "Name":"Dumbbell Romanian Deadlifts (for Upper Back)","Difficulty":"Intermediate","Primary":"Latissimus Dorsi"}
]

class Exercise(BaseModel):
    id: int
    name: str
    difficulty: str
    primary: str

@app.get("/")
async def read_root():
    return {"SetsAndReps": "API","Author":"Patrick O'Donnell","Version":".001","Docs":"http://127.0.0.1:8000/docs#","GitHub":"","Last Update": "June 10, 2024"}



@app.get("/exercises/all")
async def read_exercises(difficulty: Union[str,None] = None, primary: Union[str,None]=None):
    if difficulty or primary:
        exerciseList = exercises
        filteredList = []
        if difficulty:
            for exercise in exerciseList:
                if difficulty in exercise["Difficulty"]:
                    filteredList.append(exercise)

        if primary:
            if filteredList != []:
                exerciseList = filteredList
                filteredList = []
                
            for exercise in exerciseList:
                if primary in exercise["Primary"]:
                    filteredList.append(exercise)

        return filteredList

    return exercises

@app.get("/exercise/{id}")
async def read_exercise(id: int):
    for exercise in exercises:
        if exercise["Id"] == id:
            return exercise
    return {"Response": "Not Found"}

@app.post("/exercise")
async def add_exercise(exercise: Exercise):
    nextId = max(exercise["Id"] for exercise in exercises) + 1
    newEx = {
        "Id": nextId,
        "Name": exercise.name,
        "Difficulty": exercise.difficulty,
        "Primary": exercise.primary
    }
    exercises.append(newEx)
    return newEx

@app.get("/difficultys/")
async def read_difficulty_options():
    difficulties = list()
    for exercise in exercises:
        if exercise["Difficulty"] not in difficulties:
            difficulties.append(exercise["Difficulty"])
    difficulties.sort()
    return difficulties

@app.get("/primarymuscles/")
async def read_primary_muscles():
    primaries = list()
    for exercise in exercises:
        if exercise["Primary"] not in primaries:
            primaries.append(exercise["Primary"])
    primaries.sort()
    return primaries


