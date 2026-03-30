# app/routes/job.py
from fastapi import APIRouter
from app.core import storage

router = APIRouter(prefix="/job", tags=["Job"])

@router.post("/add")
def add_job(description: str):
    storage.job_description = description
    return {"message": "Offre ajoutée avec succès"}