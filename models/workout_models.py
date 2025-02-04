from pydantic import BaseModel
from typing import List, Dict

class AddWorkout(BaseModel):
    exercise_name : str
    date: str
    reps: int
    weight: float
    user_email: str

class ExerciseEntry(BaseModel):
    reps: int
    weight: float

class ExercisesList(BaseModel):
    entries: List[ExerciseEntry]

class WorkoutDay(BaseModel):
    exercises: Dict[str, List[ExerciseEntry]]

class Workouts(BaseModel):
    workouts: Dict[str, WorkoutDay]

class GetDay(BaseModel):
    user_email: str
    date: str

'''
Example for what we want the data structure to look like

workouts : {
    "04/02/2024" : {
        "leg press" [
            {reps: 5, weight: 30}, {reps: 4, weight: 20}
        ],
        "chest press" : [
            {reps: 5, weight: 30}, {reps: 4, weight: 20}
        ]
    },
    "05/02/2024" : {
    ***
    }
}
'''