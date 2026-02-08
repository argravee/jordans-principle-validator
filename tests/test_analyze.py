from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
def test_analyze():
    response = client.post("/analyze",files={"file": ("test.txt",b"dummy content")})
    assert response.status_code == 200
    assert response.json()["message"] == "file received"

def test_analyze_requires_file():
    response = client.post("/analyze")
    assert response.status_code == 422
