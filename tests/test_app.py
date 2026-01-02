import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_hello():
    client = app.test_client()
    reponse = client.get("/")
    assert reponse.status_code == 200
    assert b"Flask app is deployed on Azure" in response.data