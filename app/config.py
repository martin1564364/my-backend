import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv(".env")

class Settings:
    API_KEY: str = os.getenv("API_KEY", "your-secure-api-key-here")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    
    def validate_api_key(self, api_key: Optional[str]) -> bool:
        return api_key is not None and api_key == self.API_KEY

settings = Settings()