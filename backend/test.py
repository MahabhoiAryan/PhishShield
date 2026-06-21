from analyzers.url_checker import extract_urls

sample_email = """
URGENT!

Verify account now.

https://paypal-secure.xyz

Regards
"""

print(extract_urls(sample_email))