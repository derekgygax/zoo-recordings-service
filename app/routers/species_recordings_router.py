
from fastapi import APIRouter, Depends

from app.services import get_species_recordings_service
from app.services.species_recordings_service import SpeciesRecordingsService

# How to control what species are allowed!!
# Your microservices need to TALK!!

router = APIRouter(prefix="/api/v1/species_recordings")

@router.get("", response_model=str)
async def get_species_recordings(service: SpeciesRecordingsService = Depends(get_species_recordings_service)):
    return "Getting the species recordings. Sounds or Narration"

# @router.get("/{species_name}/sounds", response_model=str)
# async def get_species_sounds(species_name: str):
#     return f"Getting the species sounds for {species_name}"

# @router.post("/{species_name}/sounds", response_model=str)
# async def get_species_sounds(species_name: str):
#     return f"Getting the species sounds for {species_name}"

# @router.get("/{species_name}/narration", response_model=str)
# async def get_species_sounds(species_name: str):
#     return f"Getting the narration for {species_name}"

# @router.post("/{species_name}/narration", response_model=str)
# async def get_species_sounds(species_name: str):
#     return f"Getting the narration  for {species_name}"