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

header = {"Access-Control-Allow-Origin":"*"}

@app.get("/details")
def response():
    return myDetails, header

@app.post("/data")
def create_data(details : myDetail):
    return details.age + details.track, header


