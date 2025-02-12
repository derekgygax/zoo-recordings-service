import os
from fastapi import FastAPI

# initiative the config!!
from app.config import config

from app.routers.species_recordings_router import router as species_recordings_router

app = FastAPI()

app.include_router(species_recordings_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
	return "Welcome to the Zoo Recordings Service API"