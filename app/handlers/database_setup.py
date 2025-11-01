import json

def setup_database(event, context):
    try:
        from app.database import Base, engine
        from app.models.transaction import Transaction
        Base.metadata.create_all(bind=engine)
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Database tables created successfully"
            })
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": f"Database setup failed: {str(e)}"
            })
        }