import os
from fastapi import UploadFile

UPLOAD_DIR = "app/uploads"

def save_cv(file: UploadFile):
    """
    Sauvegarde le fichier uploadé dans uploads/ 
    et retourne le chemin du fichier.
    """
    # Crée le dossier s'il n'existe pas
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Écriture du fichier
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path