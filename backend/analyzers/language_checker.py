def detect_suspicious_words(email_text):

    suspicious_words = [
        "urgent",
        "verify",
        "suspended",
        "immediately",
        "click here",
        "password",
        "login",
        "account locked"
    ]

    found_words = []

    email_lower = email_text.lower()

    for word in suspicious_words:

        if word in email_lower:
            found_words.append(word)

    return found_words


def calculate_risk(found_words):

    score = len(found_words) * 10

    if score >= 40:
        risk = "HIGH"
    elif score >= 20:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return score, risk