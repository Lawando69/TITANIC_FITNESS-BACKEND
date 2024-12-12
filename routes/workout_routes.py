import json
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel


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