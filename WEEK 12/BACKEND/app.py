from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="Simple Fast Api App", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI application"}


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
