from fastapi import FastAPI
import copilot

app = FastAPI()

app.include_router(copilot.router)


@app.get("/")
def home():
    return {"message": "Heyyyyyyy Thereeeee!!!!"}