from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/about")
def about():
    return {"name": "Adithya", "course": "AI & DS"}

@app.get("/skills")
def skills():
    return ["Python", "SQL", "FastAPI"]  