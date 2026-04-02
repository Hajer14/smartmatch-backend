# app/routes/cv.py
from fastapi import APIRouter, UploadFile, File
from app.core import storage
from PyPDF2 import PdfReader

router = APIRouter(prefix="/cv", tags=["CV"])


# 🔥 Fonction extraction PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text


# 🔥 Fonction analyse qualité
def analyze_text_quality(text):
    print("\n========== ANALYSE TEXTE ==========")

    length = len(text)
    print(f"📏 Longueur : {length}")

    print("\n👁️ Aperçu :")
    print(text[:300])

    keywords = ["python", "sql", "data", "experience"]
    found = [word for word in keywords if word in text.lower()]

    print("\n🧠 Mots-clés trouvés :", found if found else "❌ Aucun")

    print("===================================\n")

    return {
        "length": length,
        "keywords_found": found
    }


@router.post("/upload")
async def upload_cv(file: UploadFile = File(...)):

    # 🔥 Détection type fichier
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    else:
        content = await file.read()
        text = content.decode("utf-8", errors="ignore")

    # 🔥 Analyse qualité
    analysis = analyze_text_quality(text)

    # 🚨 Vérification forte
    if analysis["length"] < 100:
        return {
            "error": "CV non exploitable (texte trop court ou mauvais parsing)",
            "analysis": analysis
        }

    # Sauvegarde
    storage.cvs_paths.append(text)

    return {
        "message": "CV ajouté avec succès",
        "total_cvs": len(storage.cvs_paths),
        "analysis": analysis
    }