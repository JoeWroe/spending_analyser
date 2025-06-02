from sqlalchemy import text

from app.database import SessionLocal

def test_database_session():
    session = SessionLocal()

    assert session is not None
    try:
        result = session.execute(text("SELECT 1"))
        assert list(result)[0][0] == 1
    finally:
        session.close()

