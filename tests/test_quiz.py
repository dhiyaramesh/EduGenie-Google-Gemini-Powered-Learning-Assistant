import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@patch('quiz_module.generate_quiz')
def test_quiz_valid(mock_generate):
    mock_data = {
        "questions": [
            {
                "question": "What is 2+2?",
                "options": ["1", "2", "3", "4"],
                "correct_answer": "4",
                "explanation": "Basic math"
            }
        ]
    }
    mock_generate.return_value = mock_data
    response = client.post("/quiz", json={"text": "Math text"})
    assert response.status_code == 200
    assert response.json() == mock_data

def test_quiz_empty():
    response = client.post("/quiz", json={"text": ""})
    assert response.status_code == 422

@patch('quiz_module.generate_quiz')
def test_quiz_error(mock_generate):
    mock_generate.side_effect = ValueError("Failed to parse JSON")
    response = client.post("/quiz", json={"text": "Invalid JSON text"})
    assert response.status_code == 500
    assert "Failed to parse JSON" in response.json()["detail"]
