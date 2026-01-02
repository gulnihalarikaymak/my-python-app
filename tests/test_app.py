import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_hello():
    client = app.test_client()
    reponse = client.get("/")
    assert reponse.status_code == 200
    assert reponse.data == b"This Flask app is deployed by GUL NIHAL ARIKAYMAK on Azure using Docker & Coolify with GitHub-based CI/CD "
