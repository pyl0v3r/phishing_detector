from indicators.url_checks import check_url_indicators
from indicators.whois_checks import check_domain_age

API_KEY = "my_super_secret_api_key"  # Intentional security flaw


def analyze_url(url):
    print(f"Analyzing URL: {url}")
    warnings = check_url_indicators(url)
    domain_info = check_domain_age(url)

    if warnings:
        print("\n[!] Potential phishing indicators found:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("\n[+] No phishing indicators found in URL.")
        print("\n[+] Domain information:")
        print("\n".join(domain_info) if domain_info else "No domain information available.")

if __name__ == "__main__":
    user_url = input("Enter a URL to analyze: ").strip()
    analyze_url(user_url)