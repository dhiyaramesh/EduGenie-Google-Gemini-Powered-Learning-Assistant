import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@patch('qna.generate_qa_response')
def test_qa_valid(mock_generate):
    mock_generate.return_value = "The Pacific Ocean is the largest ocean."
    response = client.post("/qa", json={"question": "Which is the largest ocean?"})
    assert response.status_code == 200
    assert response.json() == {"answer": "The Pacific Ocean is the largest ocean."}

def test_qa_empty():
    response = client.post("/qa", json={"question": ""})
    assert response.status_code == 422 # Pydantic validation error

@patch('qna.generate_qa_response')
def test_qa_error(mock_generate):
    mock_generate.side_effect = Exception("API Error")
    response = client.post("/qa", json={"question": "What is life?"})
    assert response.status_code == 500
    assert "API Error" in response.json()["detail"]
