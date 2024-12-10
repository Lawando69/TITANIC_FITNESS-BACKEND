from fastapi import FastAPI
from routes.workout_routes import workout_routes

app = FastAPI()

app.include_router(workout_routes,prefix="/workouts",tags=["Workouts"])

@app.get("/")
def test():
    return {"hello":"goober"}