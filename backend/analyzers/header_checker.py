def analyze_headers(email_content):

    findings = []
    risk_score = 0

    content = email_content.lower()

    if "reply-to:" in content:

        findings.append("Reply-To header detected")
        risk_score += 10

    if "return-path:" in content:

        findings.append("Return-Path header detected")
        risk_score += 10

    if "received:" in content:

        findings.append("Received header present")
        risk_score += 5

    return findings, risk_score