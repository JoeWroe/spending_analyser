import pandas as pd

from datetime import datetime

from .models.transaction import Transaction
from .database import SessionLocal

def ingest_statement_csv(file_path: str):
    statement_dataframe = pd.read_csv(file_path)
    session = SessionLocal()

    for _, row in statement_dataframe.iterrows():
        transaction = Transaction(
            transaction_id=row['Transaction ID'],
            date=datetime.strptime(row['Date'], '%d/%m/%Y').date(),
            time=datetime.strptime(row['Time'], '%H:%M:%S').time(),
            type=row['Type'],
            name=row['Name'],
            category=row['Category'],
            amount=row['Amount'],
            currency=row['Currency'],
            local_amount=row['Local amount'],
            local_currency=row['Local currency'],
            notes_and_tags=row['Notes and #tags'],
            address=row[ 'Address' ],
            description=row[ 'Description' ],
            category_split=row[ 'Category split' ],
            money_out=row[ 'Money Out' ],
            money_in=row[ 'Money In' ]
        )
        session.add(transaction)

    session.commit()
    session.close()

