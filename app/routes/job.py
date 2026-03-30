from fastapi import APIRouter

router = APIRouter(prefix="/job", tags=["Job"])
job_description = ""

@router.post("/add")
def add_job(description: str):
    global job_description
    job_description = description
    return {"message": "Offre ajoutée avec succès"}