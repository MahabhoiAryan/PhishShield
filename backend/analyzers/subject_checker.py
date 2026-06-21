def analyze_subject(subject):

    suspicious_subjects = [
        "urgent",
        "verify",
        "action required",
        "account suspended",
        "security alert",
        "immediate"
    ]

    findings = []
    risk_score = 0

    subject = subject.lower()

    for keyword in suspicious_subjects:

        if keyword in subject:

            findings.append(keyword)
            risk_score += 10

    return findings, risk_score