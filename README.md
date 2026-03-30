# SmartMatch Backend (MVP v1)

## 🚀 Overview

SmartMatch is an AI-powered backend service designed to match candidate CVs with job offer descriptions.

This MVP allows users to:

* Upload CVs (PDF format)
* Submit job descriptions
* Automatically match candidates to jobs using basic AI logic

---

## ⚙️ Tech Stack

* **Backend:** FastAPI (Python)
* **AI / NLP:** Basic text matching (extendable to OpenAI / embeddings)
* **File Handling:** PDF upload and parsing
* **API Testing:** Postman / Swagger UI

---

## 📂 Project Structure

```
smartmatch-backend/
│
├── app/
│   ├── main.py          # Entry point
│   ├── routes/          # API endpoints
│   ├── services/        # Business logic
│   └── models/          # Data models
│
├── requirements.txt
└── README.md
```

---

## 🧪 Features (MVP v1)

* Upload CVs via API
* Submit job descriptions
* Basic matching logic between CVs and jobs
* REST API structure ready for scaling

---

## ⚠️ Known Issues

* CV storage is temporary (not persisted properly)
* Matching algorithm is basic (no embeddings yet)
* No authentication system

---

## 🎯 Roadmap

* [ ] Fix CV storage (database integration)
* [ ] Improve matching with embeddings / AI
* [ ] Add authentication (JWT)
* [ ] Build frontend (Angular)
* [ ] Deploy on Azure

---

## ▶️ Run the Project

### 1. Clone repository

```
git clone https://github.com/your-username/smartmatch-backend.git
cd smartmatch-backend
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run server

```
uvicorn app.main:app --reload
```

### 5. Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 💡 Vision

This project is the foundation of a scalable SaaS platform for automated recruitment using AI.

---

## 👤 Author

Hajer Attar
AI Engineer | Data Analyst | Microsoft Certified
