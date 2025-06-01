import pytest
import pandas as pd

from io import StringIO
from unittest.mock import patch, MagicMock

from app.ingest import ingest_statement_csv


@patch("app.ingest.SessionLocal")
@patch("pandas.read_csv")
def test_ingest_statement_csv(mock_read_csv, mock_session_local):

    # Sample CSV data
    csv_data = StringIO(
        """Transaction ID,Date,Time,Type,Name,Category,Amount,Currency,Local amount,Local currency,Notes and #tags,Address,Description,Category split,Money Out,Money In
1,01/01/2023,12:00:00,Debit,Coffee Shop,Food & Drink,3.5,USD,3.5,USD,,Some Street,Coffee purchase,,3.5,0
"""
    )

    # Setup mock DataFrame
    mock_df = mock_df = pd.DataFrame(
        [
            {
                "Transaction ID": 1,
                "Date": "01/01/2023",
                "Time": "12:00:00",
                "Type": "Debit",
                "Name": "Coffee Shop",
                "Category": "Food & Drink",
                "Amount": 3.5,
                "Currency": "USD",
                "Local amount": 3.5,
                "Local currency": "USD",
                "Notes and #tags": "",
                "Address": "Some Street",
                "Description": "Coffee purchase",
                "Category split": "",
                "Money Out": 3.5,
                "Money In": 0,
            }
        ]
    )
    mock_read_csv.return_value = mock_df

    # Mock session and transaction add/commit
    mock_session = MagicMock()
    mock_session_local.return_value = mock_session

    ingest_statement_csv("fake_path.csv")

    # Assert that a transaction was added and committed
    assert mock_session.add.called
    assert mock_session.commit.called
    assert mock_session.close.called
