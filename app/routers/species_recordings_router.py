
from typing import List
from fastapi import APIRouter, Depends

from app.schemas.species_recordings_schema import SpecieRecordingsCreate, SpecieRecordingsOut, SpecieSoundCreate
from app.services import get_species_recordings_service
from app.services.species_recordings_service import SpeciesRecordingsService

# How to control what species are allowed!!
# Your microservices need to TALK!!

router = APIRouter(prefix="/api/v1/species_recordings")

@router.get("", response_model=List[SpecieRecordingsOut])
async def get_species_recordings(service: SpeciesRecordingsService = Depends(get_species_recordings_service)):
    all_recordings = await service.get_all_sepecies_recordings()
    return all_recordings

@router.post("")
async def add_specie_recording(
    specie_recording: SpecieRecordingsCreate,
    service: SpeciesRecordingsService = Depends(get_species_recordings_service)
):
    await service.insert_specie_recording(specie_recording=specie_recording)

@router.patch("/{specie_recording_id}/sound")
async def add_specie_sound_to_recording(
    specie_recording_id: str,
    sound: SpecieSoundCreate,
    service: SpeciesRecordingsService = Depends(get_species_recordings_service)
):
    await service.add_specie_sound_to_recording(specie_recording_id=specie_recording_id, sound=sound)

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