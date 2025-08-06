import re
from urllib.parse import urlparse

def check_url_indicators(url):
    indicators = []
    parsed_url = urlparse(url)

    # Check for common phishing indicators in the URL
    if(re.match(r"^(http|https)://\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}/", url)):
        indicators.append("IP address in URL")

    if "@" in url:
        indicators.append("Email address in URL")
    
    if(len(url) > 75):
        indicators.append("URL length exceeds 75 characters")

    if "-" in parsed_url.netloc:
        indicators.append("Hyphen in domain name, may imitate legitimate sites")

    if parsed_url.scheme not in ["http", "https"]:
        indicators.append("Non-standard URL scheme detected")
    
    if parsed_url.scheme == "https" and not parsed_url.netloc.endswith(".com"):
        indicators.append("HTTPS URL not ending with .com, may be suspicious")

    if parsed_url.scheme != "https":
        indicators.append("Non-HTTPS URL, may be insecure")

    suspicious_keywords = ["login", "secure", "account", "update", "verify"]
    if any(keyword in url for keyword in suspicious_keywords):
        indicators.append("Suspicious keywords found in URL")
    
    return indicators