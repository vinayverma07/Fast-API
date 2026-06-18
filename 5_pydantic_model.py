from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city:str
    state:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

#Users Route
@app.post("/create-user")
def create_user(user:User):
    return{
        "message":"User Created",
        "data":user
    }
