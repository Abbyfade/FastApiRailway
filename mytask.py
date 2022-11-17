from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

myDetails = {
    "name": "Abby",
    "Age": 20,
    "track": "Backend Python",
    "hobbies": ["watching football", "coding"]
}
class myDetail(BaseModel):
    name: str
    age: int
    track: int

@app.get("/details")
def response():
    return myDetails

@app.post("/data")
def create_data(details : myDetail):
    return details


