from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/cv", tags=["CV"])
cvs = []

@router.post("/upload")
async def upload_cv(file: UploadFile = File(...)):
    content = await file.read()
    try:
        text = content.decode("utf-8", errors="ignore")
    except:
        return {"error": "Impossible de lire le fichier"}
    cvs.append(text)
    return {"message": "CV ajouté avec succès", "total_cvs": len(cvs)}