from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base
from app import schemas
from app.config import settings
from alembic import command 

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creates all the tables in the test database
Base.metadata.create_all(bind=engine) 


def override_get_db():
    # session is responible for talking to the database
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    """ Drop all tables inside test database then recreate the tables to give
    a new slate. Then yields(return) the client to run the tests. Doing it in 
    this order pytest's flag '-x' allows you to see the state of the database 
    when the test failed.
    """
    Base.metadata.drop_all(bind=engine) 
    Base.metadata.create_all(bind=engine) 
    # using alembic if you're not going to use SQLALCHEMY
    # command.upgrade("head")
    yield TestClient(app)
    # command.downgrade("base")

def test_root(client):
    res = client.get("/")
    result = (res.json().get('message'))
    print(result) 
    assert result == "Hello World"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/",json={"email": "hello123@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json()) #preforms some of the validation based on the UserOut Mode
    # So in this case, it will make sure it has an email, password, and a created_at 
    print(new_user)
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201
