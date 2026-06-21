def analyze_sender(email_text):

    suspicious_providers = [
        "@gmail.com",
        "@yahoo.com",
        "@outlook.com",
        "@hotmail.com"
    ]

    found = []

    score = 0

    lines = email_text.split("\n")

    for line in lines:

        if "@" in line:

            email = line.strip().lower()

            for provider in suspicious_providers:

                if provider in email:

                    found.append(email)
                    score += 20

    return found, score