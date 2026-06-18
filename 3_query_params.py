from fastapi import FastAPI

app = FastAPI()

# Query Params
# /users?name=vinay
# /products?price<=1000


#Users Route
@app.get("/users")
def get_user(name: str = None):
    return {
       "Name":name
    }
