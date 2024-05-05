from fastapi.testclient import TestClient

from olympus.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_on_404():
    response = client.get("/this/route/does/not/exist")
    assert response.url.path == "/"
