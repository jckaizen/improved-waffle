from fastapi import FastAPI, status
from .database import SQLALCHEMY_DATABASE_URL
from .routers import post, user, auth, vote
from . import models
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

# No longer need since we have alembic
# Was responible for creating the tables in SQLalchemy
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',
#                 password='postgres', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection successful")
#         break
#     except Exception as error:
#         print("Failed connection to database")
#         print("Error: ", error)
#         time.sleep(3)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def main():
    print(SQLALCHEMY_DATABASE_URL)
    return {"message": "Hello World"}
