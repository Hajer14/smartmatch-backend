from fastapi import FastAPI
from app.routes import cv, job, match

app = FastAPI(
    title="SmartMatch RH AI",
    description="API de matching CV - Offre",
    version="1.0"
)

app.include_router(cv.router)
app.include_router(job.router)
app.include_router(match.router)