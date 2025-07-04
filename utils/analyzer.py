import re

def get_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    stopwords = set(["and", "the", "with", "from", "that", "this", "your", "you", "for", "are", "have"])
    return set(w for w in words if w not in stopwords)

def analyze_keywords(resume_text, job_text):
    job_keywords = get_keywords(job_text)
    resume_keywords = get_keywords(resume_text)

    matched = job_keywords & resume_keywords
    missing = job_keywords - resume_keywords

    score = int((len(matched) / len(job_keywords)) * 100) if job_keywords else 0

    suggestions = [f"Add the keyword: {word}" for word in sorted(missing)]

    return {
        "score": score,
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
        "suggestions": suggestions
    }
