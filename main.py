from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.resume_parser import extract_text_from_resume
from utils.job_parser import clean_job_description
from utils.analyzer import analyze_keywords

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    resume_file = request.files["resume"]
    job_desc = request.form["job_desc"]

    resume_text = extract_text_from_resume(resume_file)
    job_text = clean_job_description(job_desc)

    result = analyze_keywords(resume_text, job_text)
    return jsonify(result)

if __name__ == "__main__":
    app.run()