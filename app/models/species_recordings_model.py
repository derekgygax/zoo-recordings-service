from uuid import UUID
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from bson import ObjectId
from datetime import datetime

class SpecieSound(BaseModel):
    sound_id: UUID
    sound_url: str
    duration: int
    quality: str
    description: str

class Scientist(BaseModel):
    scientist_id: UUID
    name: str
    institution: str

class Narration(BaseModel):
    narration_id: UUID
    scientist: Scientist
    recording_url: str
    duration: int
    transcript: str

class SpeciesRecordings(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    species_name: str
    sounds: List[SpecieSound] = []
    narrations: List[Narration] = []

    @field_validator("id", mode="before")
    @classmethod
    def convert_objectid(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

    class Config:
        populate_by_name = True