from email import policy
from email.parser import BytesParser

def parse_eml_file(uploaded_file):

    msg = BytesParser(
        policy=policy.default
    ).parse(uploaded_file)

    sender = msg.get("From", "")
    subject = msg.get("Subject", "")

    body = ""

    if msg.is_multipart():

        for part in msg.walk():

            if part.get_content_type() == "text/plain":

                body += part.get_content()

    else:

        body = msg.get_content()

    raw_headers = ""

    for key, value in msg.items():

        raw_headers += f"{key}: {value}\n"

    return {
        "sender": sender,
        "subject": subject,
        "body": body,
        "headers": "\n".join(
            f"{k}: {v}" for k, v in msg.items()
        )
    }