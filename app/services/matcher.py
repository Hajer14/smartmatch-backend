from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_matching(cvs, job_description):
    documents = cvs + [job_description]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    job_vector = vectors[-1]
    results = []
    for i, cv_vector in enumerate(vectors[:-1]):
        score = cosine_similarity(cv_vector, job_vector)[0][0]
        results.append({"cv_id": i, "score": round(score * 100, 2)})
    return results