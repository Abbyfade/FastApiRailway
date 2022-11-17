from fastapi import FastAPI

app = FastAPI()

myDetails = {
    "name": "Abby",
    "Age": 20,
    "track": "Backend Python",
    "hobbies": {"watching football", "coding"}
}

@app.get("/details")
def response():
    return myDetails


