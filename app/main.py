import os
from fastapi import FastAPI

# initiative the config!!
from app.config import config

from app.exception_handlers import generic_exception_handler, mongo_exception_handler
from pymongo.errors import PyMongoError

from app.routers.species_recordings_router import router as species_recordings_router

app = FastAPI()

app.add_exception_handler(Exception, generic_exception_handler)
app.add_exception_handler(PyMongoError, mongo_exception_handler)

app.include_router(species_recordings_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
	return "Welcome to the Zoo Recordings Service API"