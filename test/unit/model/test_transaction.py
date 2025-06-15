from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.transaction import Transaction

def test_transaction_model_fields():
    transaction = Transaction(
        transaction_id="abc123",
        datetime=datetime(2023, 1, 1, 12, 0),
        type="Debit",
        name="Coffee Shop",
        category="Food & Drink",
        amount=3.5,
        currency="USD",
        local_amount=3.5,
        local_currency="USD",
        notes_and_tags="morning run",
        address="Some Street",
        description="Coffee purchase",
        category_split="",
        money_out=3.5,
        money_in=0
    )

    assert transaction.transaction_id == "abc123"
    assert transaction.amount == 3.5
    assert transaction.name == "Coffee Shop"


def test_transaction_model_commit():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        transaction = Transaction(
            transaction_id="txn001",
            datetime=datetime(2023, 1, 1, 12, 0),
            type="Credit",
            name="Salary",
            category="Income",
            amount=1000.0,
            currency="USD",
            local_amount=1000.0,
            local_currency="USD",
            notes_and_tags="",
            address="",
            description="Monthly salary",
            category_split="",
            money_out=0.0,
            money_in=1000.0
        )
        session.add(transaction)
        session.commit()

        retrieved = session.query(Transaction).filter_by(transaction_id="txn001").first()
        assert retrieved is not None
        assert retrieved.amount == 1000.0
    finally:
        session.close()
