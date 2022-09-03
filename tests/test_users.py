from app import schemas
from jose import jwt
import pytest
from app.config import settings


# def test_root(client):
#     res = client.get("/")
#     result = (res.json().get('message'))
#     print(result) 
#     assert result == "Hello World"
#     assert res.status_code == 200


def test_create_user(client):
    # need /users/ instead of /users bc fastapi was redirect (307 code) to /users/ when 
    # using /users
    # But here it's expecting a 201 and not a 307
    res = client.post("/users/",json={"email": "hello123@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json()) #preforms some of the validation based on the UserOut Mode
    # So in this case, it will make sure it has an email, password, and a created_at 
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201


def test_login_user(client,test_user):
    res = client.post("/login",data={"username": test_user['email'], "password":test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password,status_code", [
    ('wrongasdjfkfjklasd@gmail.com', 'password123', 403),
    ('carl@gmail.com', 'password1251', 403),
    ('carl_at_the_car_wash@gmail.com', 'carwash',403),
    (None, 'asdf',422)
    ])
def test_incorrect_login(test_user,client,email,password,status_code):
    res = client.post("/login",data={"username": email, "password": password})
    assert res.status_code == status_code 
#    assert res.json().get('detail') == 'Invalid Credentials'
