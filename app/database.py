from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import config

class MongoDB:
    _client = None
    _db = None

    # This makes the method at class level and NOT in an instance
    # cls is just the class as well, NOT a passed in param
    @classmethod
    def connect(cls):
        if cls._client is None:
            cls._client = AsyncIOMotorClient(config.MONGO_URI)
            cls._db = cls._client[config.DB_NAME]
        return cls._db

def get_db():
    return MongoDB.connect()

def get_collection(collection_name: str):
    db = get_db()
    return db[collection_name]
