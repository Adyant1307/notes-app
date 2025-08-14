import os
from motor.motor_asyncio import AsyncIOMotorClient

_client = None
_db = None

async def init_mongo():
    global _client, _db
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    dbname = os.getenv("MONGO_DB", "notesdb")
    _client = AsyncIOMotorClient(uri)
    _db = _client[dbname]

def get_db():
    if _db is None:
        raise RuntimeError("Mongo not initialized")
    return _db

async def close_mongo():
    global _client
    if _client:
        _client.close()