from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Input Schemas (for creating/updating species)
class SpecieSoundCreate(BaseModel):
    sound_url: str
    duration: int
    quality: str
    description: str

class ScientistCreate(BaseModel):
    name: str
    institution: str

class NarrationCreate(BaseModel):
    scientist: ScientistCreate
    recording_url: str
    duration: int
    transcript: str

class SpecieRecordingsCreate(BaseModel):
    species_name: str
    sounds: List[SpecieSoundCreate] = []
    narrations: List[NarrationCreate] = []

# Output Schemas (for returning species data)
class SpecieSoundOut(BaseModel):
    sound_id: UUID
    sound_url: str
    duration: int
    quality: str
    description: str

class ScientistOut(BaseModel):
    scientist_id: UUID
    name: str
    institution: str

class NarrationOut(BaseModel):
    narration_id: UUID
    scientist: ScientistOut
    recording_url: str
    duration: int
    transcript: str

class SpecieRecordingsOut(BaseModel):
    id: str
    species_name: str
    sounds: List[SpecieSoundOut]
    narrations: List[NarrationOut]