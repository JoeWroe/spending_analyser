from app.database import Base, engine
from app.models.transaction import Transaction

Base.metadata.create_all(bind=engine)
print("✅ Database and tables created.")
