from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_blogs():
  response = client.get("/blog/all")
  assert response.status_code == 200

def test_auth_errors():
  response = client.post("/token",
    data={"username": "", "password": ""}
  )
  access_token = response.json().get("access_token")
  assert access_token == None
  message = response.json().get("detail")[0].get("msg")
  assert message == "Invalid username or password."
  

def test_auth_success():
  response = client.post("/token",
    data={"username": "cat", "password": "cat1234"}
  )
  access_token = response.json().get("access_token")
  assert access_token == None