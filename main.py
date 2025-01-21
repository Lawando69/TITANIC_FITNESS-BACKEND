from fastapi import FastAPI
from routes.workout_routes import workout_routes
from routes.auth_routes import auth_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3001"], #NOTE: This ensures that we only get requests from the url mentioned (the frontend) prevents bots, better security
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(workout_routes,prefix="/workouts",tags=["Workouts"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"]) #NOTE: prefix ensures that any url entered in auth_routes, it will always start with \Auth

@app.get("/")
def test():
    return {"hello":"goober"}