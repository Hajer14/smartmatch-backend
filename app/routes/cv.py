# app/routes/cv.py
from fastapi import APIRouter, UploadFile, File
from app.core import storage

router = APIRouter(prefix="/cv", tags=["CV"])

@router.post("/upload")
async def upload_cv(file: UploadFile = File(...)):
    content = await file.read()
    try:
        text = content.decode("utf-8", errors="ignore")
    except:
        return {"error": "Impossible de lire le fichier"}

    # Sauvegarde dans le storage central
    storage.cvs_paths.append(text)

    return {"message": "CV ajouté avec succès", "total_cvs": len(storage.cvs_paths)}