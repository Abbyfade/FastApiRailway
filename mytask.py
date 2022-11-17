from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
async def response():
    return myDetails, header

@app.post("/data")
async def create_data(details : myDetail):
    return details.age + details.track


