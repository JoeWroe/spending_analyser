from sqlalchemy import Column, Integer, String, Float, DateTime
from ..database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(String, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    time = Column(DateTime, nullable=False)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    local_amount = Column(Float, nullable=False)
    local_currency = Column(String, nullable=False)
    notes_and_tags = Column(String, nullable=True)
    address = Column(String, nullable=True)
    description = Column(String, nullable=True)
    category_split = Column(String, nullable=True)
    money_out = Column(Float, nullable=True)
    money_in = Column(Float, nullable=True)
    
    
