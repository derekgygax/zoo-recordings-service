import os
from dotenv import load_dotenv

# Load .env variables in the app
load_dotenv()

class Config:
    def __init__(self):
        self.MONGO_URI = os.getenv("MONGO_URI")
        self.DB_NAME = os.getenv("MONGO_DB_NAME")
        self.SPECIES_RECORDINGS_COLLECTION = os.getenv("SPECIES_RECORDINGS_COLLECTION")
        
        ENV_VARS={
            "MONGO_URI": self.MONGO_URI,
            "MONGO_DB_NAME": self.DB_NAME,
            "SPECIES_RECORDINGS_COLLECTION": self.SPECIES_RECORDINGS_COLLECTION
        }

        missing_env_vars = [key for key, value in ENV_VARS.items() if not value]

        if missing_env_vars:
            raise ValueError(f"Missing environment variables: {', '.join(missing_env_vars)}. Check your .env file or system variables.")
        

config = Config()