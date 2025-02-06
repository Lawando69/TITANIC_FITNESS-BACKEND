import json
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from models.workout_models import AddExercise, GetDay, WorkoutDay

from .auth_routes import get_all_users, save_users


workout_routes = APIRouter()

@workout_routes.get("/")
def get_all_workouts():
    with open("./fake_db/workouts.json", "r") as file: 
        return json.load(file)


def all_workouts():
    with open("./fake_db/workouts.json", "r") as file:
        return get_all_workouts()
    
class Workout(BaseModel):
    name: str
    exercises: List[str]


@workout_routes.post("/")
def add_workout(new_workout: Workout):
    all_workouts = get_all_workouts()

    all_workouts.append(
        new_workout.model_dump()
    )

    with open("./fake_db/workouts.json", "w") as file:
        file.write(json.dumps(all_workouts, indent=4))
    
    return all_workouts

@workout_routes.post("/workout_day", response_model=WorkoutDay)
def get_workout_day(data: GetDay):
    all_users = get_all_users()

    if data.user_email not in all_users:
        raise HTTPException(404, "No user found")
    
    user = all_users[data.user_email]
    
    workouts = user["workouts"]
    day = workouts.get(data.date, {"exercises": {}}) #The brackets at the end will return and empty object
    return day

@workout_routes.post("/add_exercise")
def add_exercise(data: AddExercise):

    all_users = get_all_users()
    # NOTE: Error if the user doesn't exist
    if data.user_email not in all_users:
        raise HTTPException(404, "No user found")
    
    user = all_users[data.user_email]
    workouts = user["workouts"]
    
    # NOTE: Checks if date exists
    if data.date not in workouts:
        print("didn't find day field for this date")
        workouts[data.date] = {"exercises": {}}

    exercises = workouts[data.date]["exercises"]

    if data.exercise_name not in exercises:
        print("no existing entry for exercise, initialising with empty list")
        exercises[data.exercise_name] = []
    
    new_entry = {"reps": data.reps, "weight": data.weight}
    exercises[data.exercise_name].append(new_entry)

    save_users(all_users)

    return JSONResponse(
        status_code=201, content={"message": "Exercise added successfully"}
    )














