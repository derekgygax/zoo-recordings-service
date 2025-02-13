from bson import ObjectId
from pymongo.collection import Collection
from fastapi import HTTPException, status

import uuid

from app.schemas.species_recordings_schema import SpecieRecordingsCreate, SpecieSoundCreate
from app.models.species_recordings_model import SpeciesRecordings

class SpeciesRecordingsService:
    # The singleton decorator above ensures that this will only happen on the initial
    # intance creation. After that the same instance will always be returned
    def __init__(self, collection: Collection = None):
        self.collection = collection
    
    async def get_all_sepecies_recordings(self,):
        # The length=None tells you to return all
        # you could limit the length with 10 or 100
        all_recordings = await self.collection.find().to_list(length=None)
        return [SpeciesRecordings(**record) for record in all_recordings]

    async def get_specie_recording(self, species_name: str):
        return await self.collection.find_one({"species_name": species_name})

    async def insert_specie_recording(self, specie_recording: SpecieRecordingsCreate):
        return await self.collection.insert_one(specie_recording.model_dump())
    
    async def add_specie_sound_to_recording(self, specie_recording_id: str, sound: SpecieSoundCreate):
        if not ObjectId.is_valid(specie_recording_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID format")

        existing_recording_id = ObjectId(specie_recording_id)

        # Check the recording even exists
        existing_recording = self.collection.find_one({"_id": existing_recording_id})
        if not existing_recording:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Recording does not exist")

        sound_id = str(uuid.uuid4())
        # Add the sound to the recording
        result = await self.collection.update_one(
            {
                "_id": existing_recording_id
            }, 
            {
                "$push": {"sounds": {**sound.model_dump(), "sound_id": str(sound_id)}}
            }
        )

        if result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to add sound")


    async def update_species_recording(self, species_name: str, data: dict):
        return await self.collection.update_one(
            {"species_name": species_name},
            {"$set": data},
            upsert=True
        )

    async def delete_species_recording(self, species_name: str):
        return await self.collection.delete_one({"species_name": species_name})
