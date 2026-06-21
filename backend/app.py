from analyzers.language_checker import detect_suspicious_words, calculate_risk
from flask import Flask, render_template, request
from analyzers.eml_parser import parse_eml_file
from analyzers.subject_checker import analyze_subject
from analyzers.header_checker import analyze_headers
from database.db import create_table, save_scan

app = Flask(__name__)

create_table()

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
    uploaded_file = request.files.get("email_file")
    text_content = request.form.get("email_content", "").strip()

    if (
        (not uploaded_file or uploaded_file.filename == "")
        and text_content == ""
    ):
        return """
        <script>
            alert("Please paste email content or upload an EML file.");
            window.location.href='/';
        </script>
        """
    if uploaded_file and uploaded_file.filename.endswith(".eml"):

        parsed_email = parse_eml_file(uploaded_file)

        sender = parsed_email["sender"]
        subject = parsed_email["subject"]
        body = parsed_email["body"]
        headers = parsed_email["headers"]

        email_content = f"""
        {headers}

        {body}
        """
    else:

        email_content = text_content

    detected_words = detect_suspicious_words(email_content)

    urls = extract_urls(email_content)
    
    suspicious_urls, url_risk = check_suspicious_urls(urls)

    sender_findings, sender_risk = analyze_sender(email_content)
    print("EMAIL CONTENT SENT TO HEADER CHECKER")
    print(email_content)

    header_findings, header_risk = analyze_headers(email_content)

    url_count = len(suspicious_urls)
    
    indicator_count = len(detected_words)
    
    sender_count = len(sender_findings)
    subject_findings, subject_risk = analyze_subject(subject if 'subject' in locals() else "")
    keyword_score, _ = calculate_risk(detected_words)
    
    score = ( keyword_score + url_risk + sender_risk + subject_risk + header_risk ) 
    if score > 100:
        score = 100
    needle_angle = (score / 100) * 180 - 90
    confidence = min(score, 100)
    score = min(score, 100)
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

    save_scan(
        sender if 'sender' in locals() else "Manual Input",
        risk,
        score
    )

    badge_color = {
    "LOW": "#22c55e",
    "MEDIUM": "#facc15",
    "HIGH": "#ef4444"
}[risk]



        # return f"""
        # <!DOCTYPE html>
        # <html>

        # <head>
        # <title>PhishShield Report</title>
        # </head>

        # <body style="
        # background:#0f172a;
        # color:white;
        # font-family:Arial;
        # padding:40px;">

        # <h1>🛡️ PhishShield Analysis Report</h1>

        # <div style="
        # background:{badge_color};
        # padding:15px;
        # width:250px;
        # border-radius:10px;
        # font-weight:bold;">

        # Risk Level: {risk}

        # </div>
        # <div style="
        # display:flex;
        # gap:20px;
        # margin-top:20px;
        # margin-bottom:20px;">

        # <div style="
        # background:#1e293b;
        # padding:15px;
        # border-radius:10px;
        # width:180px;

        # text-align:center;

        # font-size:18px;

        # box-shadow:0 0 10px rgba(56,189,248,0.2);">
        # URLs Found<br>
        # <b>{url_count}</b>
        # </div>

        # <div style="
        # background:#1e293b;
        # padding:15px;
        # border-radius:10px;
        # width:180px;

        # text-align:center;

        # font-size:18px;

        # box-shadow:0 0 10px rgba(56,189,248,0.2);">
        # Indicators<br>
        # <b>{indicator_count}</b>
        # </div>

        # <div style="
        # background:#1e293b;
        # padding:15px;
        # border-radius:10px;
        # width:180px;

        # text-align:center;

        # font-size:18px;

        # box-shadow:0 0 10px rgba(56,189,248,0.2);">
        # Senders<br>
        # <b>{sender_count}</b>
        # </div>

        # </div>
        # <br>


        # <h2>Risk Score: {score}/100</h2>

        # <h3>Threat Summary</h3>

        # <p>{summary}</p>

        # <h3>Suspicious URLs</h3>

        # <ul>
        # {''.join(f'<li>{url}</li>' for url in suspicious_urls)}
        # </ul>
        
        # <h3>Suspicious Subject Indicators</h3>

        # <ul>
        # {''.join(f'<li>{item}</li>' for item in subject_findings)}
        # </ul>

        # <h3>Header Analysis</h3>

        # <ul>
        # {''.join(f'<li>{item}</li>' for item in header_findings)}

        # {"<li>No suspicious headers detected</li>" if not header_findings else ""}
        # </ul>

        # <h3>Detected Indicators</h3>
        # <ul>
        # {''.join(f'<li>{word}</li>' for word in detected_words)}
        # </ul>

        # <h3>Suspicious Senders</h3>

        # <ul>
        # {''.join(f'<li>{sender}</li>' for sender in sender_findings)}
        # </ul>

        # <br>

        # <a href="/" style="
        # color:#38bdf8;
        # text-decoration:none;
        # font-size:18px;">
        # ← Analyze Another Email
        # </a>

        # </body>

        # </html>
        # """
    return render_template(
        "report.html",

        score=score,
        needle_angle=needle_angle,

        risk=risk,
        badge_color=badge_color,

        suspicious_urls=suspicious_urls,
        detected_words=detected_words,
        sender_findings=sender_findings,
        header_findings=header_findings,
        subject_findings=subject_findings,

        url_count=url_count,
        indicator_count=indicator_count,
        sender_count=sender_count,

        summary=summary
    )
if __name__ == "__main__":
    app.run(debug=True)