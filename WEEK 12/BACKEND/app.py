from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="Simple Fast Api App", version="1.0.0")
data = [{"name": "Sam Larry", "age": 20, "track": "AI Developer"},
        {"name": "Bahubali", "age": 21, "track": "AI Engineer"},
        {"name": "John Doe", "age": 22, "track": "Frontend Developer"}]


class Item(BaseModel):
    name: str = Field(..., examples=["Sam Larry", "Bahubali"])
    age: int = Field(..., examples=[25])
    track: str = Field(..., examples=["AI Developer", "AI Engineer"])


@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI application"}


@app.get("/get-data")
def get_data():
    return data


@app.post("/create-data")
def create_data(item: Item):
    data.append(item.model_dump())
    return {"Message": "Data Created", "Data": data}


@app.put("/create-record/{id}")
def create_record(item: Item):
    data[id] = item.model_dump()
    return {"Message": "Data Record Added", "Data": data}


@app.patch("/update-record/{id}")
def update_record(id: int, item: Item):
    # first ensure record exists
    try:
        data[id].update(item.model_dump())
        return {"Message": "Data Record Updated", "Data": data}
    except IndexError:
        return {"Message": "Data Record Not Found", "Data": data}


@app.delete("/delete-record/{id}")
def delete_record(id: int):
    try:
        del data[id]
        return {"Message": "Data Record Deleted", "Data": data}
    except Exception as e:
        return {"Message": "Data Record Not Found", "Error": e}

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
