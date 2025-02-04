import json
from fastapi import APIRouter, HTTPException

from models.auth_models import LoginForm, RegisterForm

auth_router = APIRouter()

def get_all_users():
    with open("./fake_db/users.json", "r") as file:
        return json.load(file)

def save_users(new_users):
    with open("./fake_db/users.json", "w") as file:
        file.write(json.dumps(new_users, indent=4)) #NOTE: dumps will allow us to use the indent function


@auth_router.post("/register")
def register_user(register_data: RegisterForm):

    all_users = get_all_users()
    email = register_data.email

    if email in all_users:
        raise HTTPException(409, "User already exists")
    
    new_user = register_data.model_dump()
    new_user["workouts"] = {}

    all_users[email] = new_user

    save_users(all_users)
    return new_user


@auth_router.post("/login")
def login(login_data: LoginForm):

    all_users = get_all_users()
    email = login_data.email

    if email not in all_users:
        raise HTTPException(401, "Invalid Credentials") #NOTE: The raise exception runs similar to a return in a function
    if all_users[email]["password"] != login_data.password: #NOTE: The all_users[email]["password"] access the password with the email specified in all_users
        raise HTTPException(401, "Invalid Credentials") #NOTE: Instead of password, we are using credentials for better security
    return all_users[email]



