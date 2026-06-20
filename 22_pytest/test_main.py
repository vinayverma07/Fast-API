from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

#Test Home API
def test_home():
    response = client.get("/")
    #Status code check
    assert response.status_code == 200
    #Response data check
    assert response.json() == {"message":"Hello vinay"}

#Test ADD API
def test_add():
    response = client.get("/add?a=5&b=8")

    assert response.status_code == 200
    assert response.json() == {"result": 13}