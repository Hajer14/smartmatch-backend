# app/routes/match.py
from fastapi import APIRouter
from app.core import storage
from app.services.matcher import calculate_matching

router = APIRouter(prefix="/match", tags=["Matching"])

@router.get("/")
def match():
    if not storage.cvs_paths:
        return {"error": "Aucun CV uploadé"}

    if not storage.job_description:
        return {"error": "Aucune offre ajoutée"}

    results = calculate_matching(storage.cvs_paths, storage.job_description)
    return results