from app.db.mongo import get_db

async def ensure_indexes():
    db = get_db()
    await db.users.create_index("user_email", unique=True)
    await db.notes.create_index([("user_id", 1), ("created_on", -1)])