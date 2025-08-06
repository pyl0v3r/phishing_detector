
# 🛡️ Phishing URL Detection Tool (Python CLI)

## 🔍 Overview

This lightweight command-line tool helps detect potentially malicious or phishing URLs based on common red flags and structural analysis. Built in Python, it’s designed for cybersecurity learners and practitioners to bridge the gap between theoretical knowledge and hands-on detection techniques.

The tool does **not rely on machine learning or external services**, making it portable, transparent, and easy to extend.

---

## ⚙️ Features

- ✅ Detects common phishing indicators in URLs:
  - IP address in place of domain name
  - Use of `@` symbols
  - Long or obfuscated URLs
  - Hyphenated domains (e.g., `secure-login-paypal.com`)
  - Lack of HTTPS
  - Suspicious keywords in URL paths
- ✅ WHOIS-based domain age checking
- ✅ Command-line interface
- ✅ Modular Python codebase

---

## 🚀 How to Use

### 🔧 Prerequisites

Make sure the following are installed:

```bash
sudo apt update
sudo apt install python3 python3-pip whois
pip3 install requests beautifulsoup4 python-whois
```

### 📁 Project Structure

```
phishing-detector/
├── main.py
├── indicators/
│   ├── url_checks.py
│   └── whois_checks.py
└── test_urls.txt
```

### ▶️ Run the Tool

```bash
python3 main.py
```

Then enter a URL when prompted:

```text
Enter a URL to analyze: https://secure-login.example.com
```

Example Output:
```
[+] Analyzing URL: https://secure-login.example.com

[!] Potential Phishing Indicators Found:
  - Domain contains a hyphen (may imitate legit site)
  - Contains suspicious keywords
  - Domain age is less than 6 months
```

---

## 📚 Learning Outcomes

By completing and using this tool, you will:

- Understand how phishing campaigns structure deceptive URLs
- Learn to identify URL-based indicators without relying on threat feeds
- Gain experience working with Python, WHOIS lookups, and CLI tools
- Improve your ability to spot phishing scams in real-world settings

---

## 🔒 Security Mindset

This tool simulates basic detection methods used in incident response and red team assessments. It reflects best practices for recognizing phishing threats **before** they are flagged by antivirus or reputation engines.

---

## 🧭 Future Enhancements

> These features are under development or planned for future versions:

- 🔍 VirusTotal API integration for real-time threat intelligence
- 🧠 PhishTank feed parsing to detect known phishing domains
- 🔗 URL shortener detection and unmasking
- 📝 Logging and reporting to CSV for audit trails
- 🌐 HTTP header & SSL inspection
- 🧪 CLI arguments and batch URL scanning

---

## 📜 License

This project is open-source under the MIT License.

---

## ✍️ Author

**Urvashi Godumalani**  
[LinkedIn](https://www.linkedin.com/in/urvashi-godumalani-043840113/) | [GitHub](https://github.com/pyl0v3r)
