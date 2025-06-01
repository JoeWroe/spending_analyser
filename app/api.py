from fastapi import FastAPI
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models.transaction import Transaction

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/transactions")
def read_all_transactions():
    db: Session = SessionLocal()
    transactions = db.query(Transaction).all()
    db.close()
    return transactions
