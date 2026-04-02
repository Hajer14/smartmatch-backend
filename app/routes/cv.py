# app/routes/cv.py
from fastapi import APIRouter, UploadFile, File
from app.core import storage
from PyPDF2 import PdfReader

router = APIRouter(prefix="/cv", tags=["CV"])


# 🔥 Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    # Iterate through all pages and extract text
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text


# 🔥 Function to analyze text quality
def analyze_text_quality(text):
    print("\n========== TEXT ANALYSIS ==========")

    length = len(text)
    print(f"📏 Text length: {length}")

    print("\n👁️ Preview:")
    print(text[:300])

    # Define keywords to search
    keywords = ["python", "sql", "data", "experience"]
    found = [word for word in keywords if word in text.lower()]

    print("\n🧠 Keywords found:", found if found else "❌ None")
    print("===================================\n")

    return {
        "length": length,
        "keywords_found": found
    }


# 🔥 Function to detect ATS-friendly CVs (enterprise-level)
def is_ats_friendly(text):
    """
    Advanced ATS-friendly detection:
    - Average line length
    - Presence of special characters / tabs
    - Presence of standard sections
    - Words per line ratio
    Returns True if ATS-friendly, False otherwise
    """

    # Clean and filter lines
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if not lines:
        return False

    # 1️⃣ Average line length
    avg_line_length = sum(len(line) for line in lines) / len(lines)
    if avg_line_length < 30:
        return False

    # 2️⃣ Check for special characters / tabs
    special_chars = ["\t", "|", "■", "●", "•"]
    if any(char in text for char in special_chars):
        return False

    # 3️⃣ Check for standard sections in CV
    sections = ["experience", "education", "skills", "projects", "certification"]
    found_sections = sum(1 for sec in sections if sec in text.lower())
    if found_sections < 2:
        return False

    # 4️⃣ Words per line ratio (to detect graphical CV)
    total_words = sum(len(line.split()) for line in lines)
    words_per_line = total_words / len(lines)
    if words_per_line < 3:
        return False

    # ✅ Passed all checks → ATS-friendly
    return True


@router.post("/upload")
async def upload_cv(file: UploadFile = File(...)):

    # 🔍 Extract text from uploaded file
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    else:
        content = await file.read()
        text = content.decode("utf-8", errors="ignore")

    # 🧠 Analyze text quality
    analysis = analyze_text_quality(text)

    # 🔥 Compute quality score
    score_quality = 0
    if len(text) > 1000:
        score_quality += 1
    if len(analysis["keywords_found"]) >= 3:
        score_quality += 1
    if "experience" in text.lower():
        score_quality += 1

    # 🚨 Check for low-quality CV
    if score_quality < 2:
        return {
            "error": "Low-quality CV",
            "score_quality": score_quality,
            "analysis": analysis
        }

    # 🔎 Detect ATS-friendly CV
    ats_friendly = "Yes" if is_ats_friendly(text) else "No"

    # 💾 Save CV text in storage
    storage.cvs_paths.append(text)

    # ✅ Return response
    return {
        "message": "CV successfully added",
        "total_cvs": len(storage.cvs_paths),
        "analysis": analysis,
        "score_quality": score_quality,
        "ats_friendly": ats_friendly
    }