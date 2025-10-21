from sqlalchemy.testing.pickleable import User

from database import db_session
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
import bcrypt
user = {
    "name": "Samuel Dasaolu",
    "email": "samueldasaolu40@gmail.com",
    "password": "admin",
}
# try:
#     # check if user already exists
#     check_query = text("SELECT * FROM users WHERE email = :email")
#     is_existing = db_session.execute(check_query, {"email": user['email']}).fetchone()
#
#     print("\n", is_existing, "\n ")
#     if is_existing is not None:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     else:
#         query = text("INSERT INTO users (name, password, email) VALUES (:name, :password, :email)")
#
#         salt = bcrypt.gensalt()
#         hashed_password = bcrypt.hashpw(user['password'].encode('utf-8'), salt)
#
#         db_session.execute(query, {"name": user['name'], "password": hashed_password, "email": user['email']})
#         db_session.commit()
#         print({"Message": "User Created Successfully", "data": user})
#
# except Exception as e:
#     print({"Message": "An error occurred while creating User", "Error": str(e)})
# finally:
#     db_session.close()

# try:
#     query = text("SELECT * FROM users where id = 19")
#
#     results = db_session.execute(query).fetchone()
#     users = results._asdict()
#     # users = [{"id": row.id, "name": row.name, "email": row.email} for row in results]
#     if users:
#         print(users)
#
#     #     print({"Message": "Successful Request", "data": users})
#     # else:
#     #     print({'message': 'No users found', 'data': users})
#
# except Exception as e:
#     raise HTTPException(status_code=500, detail=str(e))
# finally:
#     db_session.close()
