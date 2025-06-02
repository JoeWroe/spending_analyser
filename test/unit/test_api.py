import pytest

from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from app.api import app

@patch("app.api.SessionLocal")
def test_read_all_transactions_endpoint(mock_session_local):
   # Mock the session and its query
    mock_session = MagicMock()
    mock_session.query().all.return_value = [
        {
            "id": 1,
            "transaction_id": "1",
            "date": "2023-01-01",
            "time": "12:00:00",
            "type": "Debit",
            "name": "Coffee Shop",
            "category": "Food & Drink",
            "amount": 3.5,
            "currency": "USD",
            "local_amount": 3.5,
            "local_currency": "USD",
            "notes_and_tags": "",
            "address": "Some Street",
            "description": "Coffee purchase",
            "category_split": "",
            "money_out": 3.5,
            "money_in": 0
        }
    ]
    mock_session_local.return_value = mock_session

    client = TestClient(app)
    response = client.get("/transactions")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["name"] == "Coffee Shop"
