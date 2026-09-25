import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@patch('summary_module.generate_summary')
def test_summary_valid(mock_generate):
    mock_generate.return_value = "This is a summary."
    response = client.post("/summarize", json={"text": "Very long text..."})
    assert response.status_code == 200
    assert response.json() == {"summary": "This is a summary."}

def test_summary_empty():
    response = client.post("/summarize", json={"text": ""})
    assert response.status_code == 422
