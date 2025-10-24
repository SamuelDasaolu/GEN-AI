from database import db_session
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal, Optional
from dotenv import load_dotenv
from sqlalchemy import text
import os
import uvicorn
import bcrypt

load_dotenv()
app = FastAPI(title="Simple App", version="1.0")


class User(BaseModel):
    name: str = Field(examples=['Samuel'])
    password: str = Field()
    email: str = Field(examples=['name@domain.com'])
    userType: Optional[Literal["student", "teacher", "admin"]] = Field(default="student", examples=['student'])


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class LoginRequest(BaseModel):
    email: str = Field(..., examples=["name@domain.com"])
    password: str = Field(..., examples=["password123"])


class Course(BaseModel):
    title: str = Field(examples=['Samuel'])
    level: Literal[100, 200, 300, 400, 500, 600] = Field(examples=[100 - 600])


class Entry(BaseModel):
    userId: int = Field(...)
    courseId: int = Field(...)


@app.get("/users")
def get_users():
    try:
        query = text("SELECT * FROM users")

        results = db_session.execute(query)
        users = [dict(row._mapping) for row in results]
        if users:
            return {"Message": "Successful Request", "data": users}
        else:
            return {'message': 'No users found', 'data': users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db_session.close()


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    try:
        query = text("SELECT * FROM users WHERE id = :userId")
        user = db_session.execute(query, {"userId": user_id}).fetchone()
        return {"Message": "Successful Request", "data": user._asdict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db_session.close()


@app.post("/users/signup")
def create_user(user: User):
    try:
        # check if user already exists
        check_query = text("SELECT * FROM users WHERE email = :email")
        is_existing = db_session.execute(check_query, {"email": user.email}).fetchone()
        if is_existing is not None:
            raise HTTPException(status_code=400, detail="Email already registered")

        query = text("INSERT INTO users (name, password, email) VALUES (:name, :password, :email)")
        if user.userType != "student":
            query = text(
                "INSERT INTO users (name, password, email, userType) VALUES (:name, :password, :email, :userType)")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt)

        db_session.execute(query, {"name": user.name, "password": hashed_password, "email": user.email,
                                   "userType": user.userType})
        db_session.commit()
        return {"Message": "User Created Successfully", "data": user.model_dump()}
    except Exception as e:
        db_session.rollback()
        return {"Message": "An error occurred while creating User", "Error": str(e)}
    finally:
        db_session.close()


@app.post("/users/login")
def login_user(user: LoginRequest):
    try:
        query = text("SELECT * FROM users WHERE email = :email")
        db_user = db_session.execute(query, {"email": user.email}).fetchone()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password):
            raise HTTPException(status_code=404, detail="Incorrect password")

        return {"Message": "Login Successful", "data": db_user.model_dump()}


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.patch("/users/update/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    # check for existing user
    check_query = text("SELECT * FROM users WHERE id = :id")
    existing_user = db_session.execute(check_query, {"id": user_id}).fetchone()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")

    # trying to dynamically build the query such that it's only attributes that have been supplied are considere
    # format: UPDATE users SET {set_clases} e.g SET name = :name, email = :email WHERE id = :id
    # store params and set clauses
    params = {"id": user_id}
    set_clauses = []

    update_data = user.model_dump(exclude_unset=True)

    if not update_data:
        return {'message': 'No Fields to Update', 'data': {existing_user._asdict()}}

    for key, value in update_data.items():
        if key == 'password':
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(value.encode('utf-8'), salt)

            set_clauses.append("password = :password ")
            params["password"] = hashed_password
        else:
            # Add the other fields normally
            set_clauses.append(f"{key} = :{key}")
            params.update({key: value})

    # create final query string
    try:
        query_string = f"UPDATE users SET {', '.join(set_clauses)} WHERE id = :id"
        query = text(query_string)

        db_session.execute(query, params)
        db_session.commit()

        # fetch and return updated user
        updated_user = db_session.execute(check_query, {"id": user_id}).fetchone()

        return {"Message": "User Updated Successfully", "data": updated_user._asdict()}
    except Exception as e:
        db_session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db_session.close()


@app.delete("/users/delete/{user_id}")
def delete_user(user_id: int):
    try:
        check_query = text("SELECT * FROM users WHERE id = :id")
        existing_user = db_session.execute(check_query, {"id": user_id}).fetchone()
        if existing_user is None:
            raise HTTPException(status_code=404, detail="User Does not Exist")
        query = text("DELETE FROM users WHERE id = :id")
        db_session.execute(query, {"id": user_id})
        db_session.commit()
        return {"Message": "User Deleted Successfully", "data": existing_user._asdict()}
    except Exception as e:
        db_session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db_session.close()


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
