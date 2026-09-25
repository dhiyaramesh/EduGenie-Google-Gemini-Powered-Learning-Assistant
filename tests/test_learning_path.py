import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@patch('learning_path.generate_learning_path')
def test_learning_path_valid(mock_generate):
    mock_generate.return_value = "Beginner -> Intermediate -> Advanced"
    response = client.post("/learn/recommendations", json={"topic": "SQL", "level": "Beginner"})
    assert response.status_code == 200
    assert response.json() == {"path": "Beginner -> Intermediate -> Advanced"}

def test_learning_path_empty():
    response = client.post("/learn/recommendations", json={"topic": ""})
    assert response.status_code == 422
