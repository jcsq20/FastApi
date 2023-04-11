from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class Pets(BaseModel):
    name: str
    age: int
    address: str | None = None
    price: float
    skills: List[str] = []


users = [{
    "Code":1,
    "name": "pedro",
    "lastname": "martinez",
    "age": 23
},
{
    "Code":2,
    "name": "juan",
    "lastname": "suarez",
    "age": 23
}]

@app.get("/users", summary="Get the users in the system")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user_id == user["Code"]:
            return  user
    return "User not exist"

@app.post("/users")
def create_user(name: str, lastname: str, age: int):
    code_users = []
    for user in users:
        code_users.append(user["Code"])
    code_users.sort(reverse=True)
    user_struc = {
        "Code":code_users[0]+1,
        "name": name,
        "lastname": lastname,
        "age": age
    }
    users.append(user_struc)
    return f"user {name} created"

#@app.post("/pets", response_model=Pets, summary="Create an Pet")
@app.post("/pets", summary="Create an Pet")
def create_pet(pet: Pets):
    print(pet)
    return f"create Pet {pet}"

@app.put("/users/{user_id}")
def put_user(user_id: int, name: str, lastname: str, age: int ):
    for user in users:
        if user_id == user["Code"]:
            if name != "":
                user["name"] = name
            if lastname != "":
                user["lastname"] = lastname
            if age != "":
                user["age"] = age
            return user
    return "User not existing"

@app.put("/users/{user_id}")
def put_user(user_id: int, name: str, lastname: str, age: int ):
    if name != "" and lastname != "" and age != "":
        for user in users:
            if user_id == user["Code"]:
                user["name"] = name
                user["lastname"] = lastname
                user["age"] = age
                return user
        return "User not existing"
    return "Params Empties"

@app.patch("/users/{user_id}")
def put_user(user_id: int, name: str, lastname: str, age: int ):
    for user in users:
        if user_id == user["Code"]:
            if name != "":
                user["name"] = name
            if lastname != "":
                user["lastname"] = lastname
            if age != "":
                user["age"] = age
            return user
    return "User not existing"

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user_id == user["Code"]:
            users.remove(user)
            return users
    return "User not existing"