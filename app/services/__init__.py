from pymongo.collection import Collection
from app.config import config
from app.database import get_collection
from app.services.species_recordings_service import SpeciesRecordingsService

def get_species_recordings_service():
    collection: Collection = get_collection(config.SPECIES_RECORDINGS_COLLECTION)
    return SpeciesRecordingsService(collection)