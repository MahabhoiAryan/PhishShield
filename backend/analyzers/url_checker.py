import re

def extract_urls(email_text):

    pattern = r'https?://[^\s]+'

    return re.findall(pattern, email_text)


def check_suspicious_urls(urls):

    suspicious_urls = []

    risk_points = 0

    suspicious_tlds = [
        ".xyz",
        ".top",
        ".click",
        ".tk",
        ".xyz",
        ".buzz",
        ".shop",
        ".top",
        ".club",
        ".site",
        ".online",
        ".space",
        ".link",
        ".support",
        ".live",
        ".pics",
        ".pub",
        ".info",
        ".me",
        ".cc",
        ".ru",
        ".cn",
        ".il",
        ".win",
        ".bid",
        ".trade",
        ".mobi",
        ".date",
        ".su",
        ".gdn",
        ".tech",
        ".eu",
        ".us",
        ".pw",
        ".pro",
        ".id"
    ]

    for url in urls:

        for tld in suspicious_tlds:

            if tld in url:

                suspicious_urls.append(url)
                risk_points += 20
                break

    return suspicious_urls, risk_points