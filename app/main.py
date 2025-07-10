from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.auth import verify_api_key
from app.config import settings
import logging

logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL.upper()))
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Personal Backend API",
    description="A simple backend API for personal use",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check(api_key: str = Depends(verify_api_key)):
    logger.info("Health check endpoint accessed")
    return {"message": "Everything looks great!"}

@app.get("/")
async def root():
    return {"message": "Personal Backend API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)