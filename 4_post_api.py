from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int

#Users Route
@app.post("/create-user")
# def create_user(name: str, age: int):
#     return {
#         "Name":name,
#         "Age":age
#     }

def create_user(user:User):
    return{
        "message":"User Created",
        "data":user
    }
