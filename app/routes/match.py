from fastapi import APIRouter
from app.routes.cv import cvs
from app.routes.job import job_description
from app.services.matcher import calculate_matching

router = APIRouter(prefix="/match", tags=["Matching"])

@router.get("/")
def match():
    if not cvs:
        return {"error": "Aucun CV uploadé"}
    if not job_description:
        return {"error": "Aucune offre ajoutée"}
    results = calculate_matching(cvs, job_description)
    return results