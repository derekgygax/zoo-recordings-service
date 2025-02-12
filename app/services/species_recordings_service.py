from pymongo.collection import Collection

from app.decorators import singleton

# The service is defined as a singleton class
# to ensure the collection and other global
# stuff is shared correctly
@singleton
class SpeciesRecordingsService:
    # The singleton decorator above ensures that this will only happen on the initial
    # intance creation. After that the same instance will always be returned
    def __init__(self, collection: Collection = None):
        self.collection = collection

    async def get_species_recording(self, species_name: str):
        return await self.collection.find_one({"species_name": species_name})

    async def insert_species_recording(self, data: dict):
        return await self.collection.insert_one(data)

    async def update_species_recording(self, species_name: str, data: dict):
        return await self.collection.update_one(
            {"species_name": species_name},
            {"$set": data},
            upsert=True
        )

    async def delete_species_recording(self, species_name: str):
        return await self.collection.delete_one({"species_name": species_name})
