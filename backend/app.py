from analyzers.language_checker import detect_suspicious_words, calculate_risk
from flask import Flask, render_template, request

from analyzers.url_checker import (
    extract_urls,
    check_suspicious_urls
)

from analyzers.threat_summary import generate_summary

from analyzers.sender_checker import analyze_sender

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/analyze", methods=["POST"])
def analyze():

    email_content = request.form["email_content"]

    detected_words = detect_suspicious_words(email_content)

    urls = extract_urls(email_content)
    
    suspicious_urls, url_risk = check_suspicious_urls(urls)

    sender_findings, sender_risk = analyze_sender(email_content)

    uploaded_file = request.files.get("email_file")

    print(uploaded_file)

    url_count = len(suspicious_urls)
    
    indicator_count = len(detected_words)
    
    sender_count = len(sender_findings)

    keyword_score, _ = calculate_risk(detected_words)
    score = keyword_score + url_risk + sender_risk
    if score >= 40:
        risk = "HIGH"
    elif score >= 20:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    summary = generate_summary(
    risk,
    detected_words,
    suspicious_urls
)

    badge_color = {
    "LOW": "#22c55e",
    "MEDIUM": "#facc15",
    "HIGH": "#ef4444"
}[risk]



    return f"""
    <!DOCTYPE html>
    <html>

    <head>
    <title>PhishShield Report</title>
    </head>

    <body style="
    background:#0f172a;
    color:white;
    font-family:Arial;
    padding:40px;">

    <h1>🛡️ PhishShield Analysis Report</h1>

    <div style="
    background:{badge_color};
    padding:15px;
    width:250px;
    border-radius:10px;
    font-weight:bold;">

    Risk Level: {risk}

    </div>
    <div style="
    display:flex;
    gap:20px;
    margin-top:20px;
    margin-bottom:20px;">

    <div style="
    background:#1e293b;
    padding:15px;
    border-radius:10px;
    width:180px;

    text-align:center;

    font-size:18px;

    box-shadow:0 0 10px rgba(56,189,248,0.2);">
    URLs Found<br>
    <b>{url_count}</b>
    </div>

    <div style="
    background:#1e293b;
    padding:15px;
    border-radius:10px;
    width:180px;

    text-align:center;

    font-size:18px;

    box-shadow:0 0 10px rgba(56,189,248,0.2);">
    Indicators<br>
    <b>{indicator_count}</b>
    </div>

    <div style="
    background:#1e293b;
    padding:15px;
    border-radius:10px;
    width:180px;

    text-align:center;

    font-size:18px;

    box-shadow:0 0 10px rgba(56,189,248,0.2);">
    Senders<br>
    <b>{sender_count}</b>
    </div>

    </div>
    <br>


    <h2>Risk Score: {score}/100</h2>

    <h3>Threat Summary</h3>

    <p>{summary}</p>

    <h3>Suspicious URLs</h3>

    <ul>
    {''.join(f'<li>{url}</li>' for url in suspicious_urls)}
    </ul>

    <h3>Detected Indicators</h3>
    <ul>
    {''.join(f'<li>{word}</li>' for word in detected_words)}
    </ul>

    <h3>Suspicious Senders</h3>

    <ul>
    {''.join(f'<li>{sender}</li>' for sender in sender_findings)}
    </ul>

    <br>

    <a href="/" style="
    color:#38bdf8;
    text-decoration:none;
    font-size:18px;">
    ← Analyze Another Email
    </a>

    </body>

    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)