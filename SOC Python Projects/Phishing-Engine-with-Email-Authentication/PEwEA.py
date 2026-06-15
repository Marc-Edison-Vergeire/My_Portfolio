import re
import os
import sys
import json
import base64
import urllib.request
import urllib.error
from email import message_from_string

# =========================================================================
# 🔑 ENTERPRISE API CONFIGURATION
# Register for a free developer account at https://www.virustotal.com/ to get your key.
# Paste your key within the quotation marks below. 
# If left blank "", the engine will skip the check gracefully without crashing.
# =========================================================================
VIRUSTOTAL_API_KEY = "API KEY HERE FROM YOUR VIRUSTOTAL"
# =========================================================================

def check_virustotal(url, api_key):
    """Queries VirusTotal API v3 for a given URL's security reputation."""
    if not api_key or "YOUR_" in api_key or api_key.strip() == "":
        return "⚠️ Skipped [API Key Missing]"
    try:
        # VirusTotal v3 URL endpoints require an unpadded base64 representation of the URL
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        req_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
        
        req = urllib.request.Request(req_url)
        req.add_header("x-apikey", api_key)
        
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
            malicious = stats.get("malicious", 0)
            suspicious = stats.get("suspicious", 0)
            harmless = stats.get("harmless", 0)
            
            if malicious > 0:
                return f"❌ MALICIOUS [Flagged by {malicious} security vendors]"
            elif suspicious > 0:
                return f"⚠️ SUSPICIOUS [Flagged by {suspicious} vendors]"
            return f"✅ CLEAN [Verified safe by {harmless} vendors]"
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "❔ Unrated https://tax.vermont.gov/bs/individuals/refund"
        if e.code == 401 or e.code == 403:
            return "❌ Access Denied [Invalid/Expired API Key]"
        return f"❌ HTTP Error ({e.code})"
    except Exception as e:
        return f"❌ Lookup Failed [{str(e)}]"


def parse_authentication_headers(msg):
    """
    Surgically extracts SPF, DKIM, and DMARC results from the raw email headers
    using defensive regex pattern matching.
    """
    spf_status = "NOT FOUND"
    dkim_status = "NOT FOUND"
    dmarc_status = "NOT FOUND"
    
    # Target standard security architecture authentication strings
    auth_headers = msg.get_all('Authentication-Results', []) or []
    for header in auth_headers:
        # Flatten header lines to prevent multiline regex bypasses
        header_clean = header.lower().replace('\n', ' ').replace('\r', ' ')
        
        if spf_status == "NOT FOUND":
            spf_match = re.search(r'\bspf=([a-z]+)', header_clean)
            if spf_match: spf_status = spf_match.group(1).upper()
            
        if dkim_status == "NOT FOUND":
            dkim_match = re.search(r'\bdkim=([a-z]+)', header_clean)
            if dkim_match: dkim_status = dkim_match.group(1).upper()
            
        if dmarc_status == "NOT FOUND":
            dmarc_match = re.search(r'\bdmarc=([a-z]+)', header_clean)
            if dmarc_match: dmarc_status = dmarc_match.group(1).upper()

    # Fallback to legacy Received-SPF validation layer if primary extraction yielded nothing
    if spf_status == "NOT FOUND":
        received_spf = msg.get_all('Received-SPF', []) or []
        for header in received_spf:
            header_clean = header.lower()
            if 'pass' in header_clean: spf_status = "PASS"
            elif 'fail' in header_clean: spf_status = "FAIL"
            elif 'softfail' in header_clean: spf_status = "SOFTFAIL"
            elif 'neutral' in header_clean: spf_status = "NEUTRAL"
            if spf_status != "NOT FOUND": break

    # Map status outputs to clean tactical visual indicators
    def get_status_icon(status):
        if status == "PASS": return f"✅ {status}"
        if status in ["FAIL", "HARDFAIL"]: return f"❌ {status} [HIGH RISK]"
        if status in ["SOFTFAIL", "NEUTRAL", "NONE"]: return f"⚠️ {status} [UNVERIFIED]"
        return f"❔ {status}"

    print("--- 🔐 PROTOCOL AUTHENTICATION CHECKS ---")
    print(f" 🛡️  SPF (Sender Policy Framework):     {get_status_icon(spf_status)}")
    print(f" 🛡️  DKIM (DomainKeys Identified Mail):  {get_status_icon(dkim_status)}")
    print(f" 🛡️  DMARC (Domain Authentication Policy): {get_status_icon(dmarc_status)}\n")


def analyze_phishing_email(raw_email):
    """Parses and analyzes the raw email content for security risks."""
    msg = message_from_string(raw_email)
    
    print("\n" + "=" * 25 + " [🚨 SOC PHISHING ANALYSIS REPORT] " + "=" * 25)
    print(f"🔹 Subject:   {msg.get('Subject', '[NO SUBJECT FOUND]')}")
    print(f"🔹 From:      {msg.get('From', '[NO SENDER FOUND]')}")
    print(f"🔹 To:        {msg.get('To', '[NO RECIPIENT FOUND]')}")
    
    # Extract Routing IP
    source_ip = msg.get('X-Sender-IP')
    if not source_ip:
        received_headers = msg.get_all('Received', []) or []
        for header in received_headers:
            ip_match = re.search(r'\[([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\]', header)
            if ip_match:
                source_ip = f"{ip_match.group(1)} (Extracted via Received Path)"
                break
    print(f"🔹 Source IP: {source_ip or 'Unknown / Cloud Routed'}\n")
    
    # Run Security Authentication Verification Layer
    parse_authentication_headers(msg)
    
    # Extract Email Body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ["text/html", "text/plain"]:
                payload = part.get_payload(decode=True)
                if payload:
                    body += payload.decode('utf-8', errors='ignore')
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode('utf-8', errors='ignore')
            
    # Extract Links
    links = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', body) + re.findall(r'(https?://[^\s<>"\']+)', body)))
    
    print("--- 🔗 EXTRACTED LINKS FOR TRIAGE & REPUTATION CHECK ---")
    if links:
        for idx, url in enumerate(links, 1):
            print(f" [{idx}] -> {url}")
            # Run the VirusTotal OSINT lookup
            vt_status = check_virustotal(url, VIRUSTOTAL_API_KEY)
            print(f"      ↳ 🛡️ VirusTotal: {vt_status}\n")
    else:
        print("[*] No active hyperlinks found in the email body.\n")
        
    # Heuristics Configuration Block
    print("--- ⚠️ SOCIAL ENGINEERING HEURISTICS ---")
    
    # Comprehensive, threat-mapped keyword groups
    keywords = [
        # Group 1: Psychological Urgency, Coercion, and Fear Baiting
        "critical", "action required", "compromised", "verify", "password", "urgent", "login", 
        "suspend", "sign-in", "immediate", "alert", "unauthorized", "blocked", "terminated", 
        "expiration", "expired", "deactivated", "final notice", "restricted", "discrepancy",
        
        # Group 2: Financial/Invoice Fraud (Targeting accounting and wire transfers)
        "invoice", "billing", "payment", "receipt", "wire transfer", "refund", "overdue", 
        "ach", "purchase order", "po #", "bank statement", "remittance", "direct deposit",
        
        # Group 3: Core IT, MFA, Helpdesk, and Administrative Spoofing
        "security alert", "mfa", "2fa", "passcode", "reset", "recovery", "security team", 
        "helpdesk", "admin", "it support", "microsoft", "o365", "google workspace", "re-authenticate",
        
        # Group 4: Human Resources & Document Delivery Manipulation (Corporate Bait)
        "payroll", "bonus", "salary", "benefits", "performance review", "confidential", 
        "shared document", "onedrive", "sharepoint", "docusign", "attachment", "e-sign",
        
        # Group 5: Executive Impersonation & CEO Fraud (Authority Trigger)
        "quick favor", "are you at your desk", "discreet", "confidential request", "out of the office", "in a meeting", 
        "wire immediately", "acquire gift cards", "stream card", "apple voucher", "unfamiliar vendor", "supply chain",
        
        # Group 6: The Logistics & Supply Chain Trap (Curiosity & Anxiety Bait)
        "failed delivery", "missed delivery", "tracking number", "waybill", "shipment delayed", "held at customs", 
        "postage due", "address correction", "dhl", "fedex", "ups", "usps tracking", "amazon",
        
        # Group 7: Legal, Compliance, & Regulatory Scares (Intimidation & Fear)
        "subpoena", "court order", "lawsuit", "legal proceedings", "compliance validation", "regulatory audit", "non-disclosure", "nda", "non-disclosure agreement", "tax evasion", "irs settlement",
        
        # Group 8: Modern SaaS & Trust Architecture Spoofing (Implicit Trust)
        "api key leaked", "token expiration", "okta verify", "duo prompt", "mfa bypass", "zoom meeting", "teams invite", "slack workspace", "quarantine notice", "spam digest", "link", "github security", "repository alert",
        
        # Group 9: Crypto, Web3, & Financial Incentives (Greed & Novelty)
        "airdrop", "claim token", "crypto wallet", "seed phrase", "metamask", "unclaimed funds", "reimbursement allowance", "equity grant", "stock options"
    ]
    
    # Analyze both the subject line and the body content for exact keyword matches
    search_space = (str(msg['Subject']) + " " + body).lower()
    matches = list(set([w for w in keywords if w in search_space]))
    
    if matches:
        print(f"[🚨 SUSPICIOUS] Urgent indicators detected ({len(matches)} matched): {matches}")
    else:
        print("[✅ CLEAN] No obvious urgency or social engineering keywords matched.")
    print("=" * 82 + "\n")


def find_the_email_file(script_directory):
    """Scans defensively for the target email file using multiple fallbacks."""
    common_names = ["email_to_analyze.txt", "email_to_analyze", "email_to_analyze.eml", "email.txt"]
    for name in common_names:
        full_path = os.path.join(script_directory, name)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            return full_path

    all_files = os.listdir(script_directory)
    for file in all_files:
        if file.endswith((".txt", ".eml")) and file != "requirements.txt" and not file.endswith(".py"):
            return os.path.join(script_directory, file)
    return None


def main():
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    print("[*] Diagnostic: Script running folder -> " + SCRIPT_DIR + "\n")
    
    target_file_path = find_the_email_file(SCRIPT_DIR)
    
    if not target_file_path:
        default_path = os.path.join(SCRIPT_DIR, "email_to_analyze.txt")
        with open(default_path, "w", encoding="utf-8") as f:
            f.write("DELETE THIS LINE AND PASTE YOUR RAW EMAIL TEXT HERE")
            
        print(f"[!] Target email file was missing. Created template at:")
        print(f"    -> {default_path}")
        print("\n[🎯 ACTION REQUIRED]: Open 'email_to_analyze.txt' in VSCode, paste email raw content, save, and run again.")
        return

    print(f"[+] Processing target asset: {os.path.basename(target_file_path)}")
    
    with open(target_file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if "DELETE THIS LINE" in content or not content.strip():
        print("[-] Error: The file is empty or contains placeholder text. Please paste valid raw email data.")
        return

    analyze_phishing_email(content)

if __name__ == "__main__":
    main()