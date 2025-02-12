from typing import Collection
from app.config import config
from app.database import get_collection
from app.services.species_recordings_service import SpeciesRecordingsService

async def get_species_recordings_service():
    collection: Collection = await get_collection(config.SPECIES_RECORDINGS_COLLECTION)
    return SpeciesRecordingsService(collection)