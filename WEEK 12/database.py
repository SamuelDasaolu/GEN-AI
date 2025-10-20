from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# db_url_format = dialect+driver://dbuser;dbpasswd;dbhost;dbport;dbname
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
# print(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT)
#
db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(f"db_url : {db_url}")

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
db_session = Session()

query = text("SELECT * FROM users")
users = db_session.execute(query).fetchall()
print(users)
