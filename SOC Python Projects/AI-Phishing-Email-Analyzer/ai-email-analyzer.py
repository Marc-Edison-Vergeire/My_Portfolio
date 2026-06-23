ascii=r"""

   ___   ____    ________  _____    ___             __         __     ______          __
  / _ | /  _/   / __/ __ \/ ___/   / _ | ___  ___ _/ /_ _____ / /_   /_  __/__  ___  / /
 / __ |_/ /    _\ \/ /_/ / /__    / __ |/ _ \/ _ `/ / // (_-</ __/    / / / _ \/ _ \/ / 
/_/ |_/___/   /___/\____/\___/   /_/ |_/_//_/\_,_/_/\_, /___/\__/    /_/  \___/\___/_/  
                                                   /___/                                

                             by Marc Edison Vergeire
				     2026
"""

print(ascii)

import re
import os
import sys
import json
import base64
import urllib.request
import urllib.error
from email import message_from_string
from google import genai
from google.genai import types

# =========================================================================
# 🔑 ENTERPRISE API CONFIGURATIONS
# =========================================================================
GEMINI_API_KEY = "YOUR_ACQUIRED_API_KEY_HERE"
VIRUSTOTAL_API_KEY = "YOUR_ACQUIRED_API_KEY_HERE"
# =========================================================================

def check_virustotal(url, api_key):
    """Queries VirusTotal API v3 for a given URL's security reputation."""
    if not api_key or "YOUR_" in api_key or api_key.strip() == "":
        return "⚠️ Skipped [API Key Missing]"
    try:
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
            return "❔ Unrated / Unknown by VirusTotal"
        if e.code == 401 or e.code == 403:
            return "❌ Access Denied [Invalid/Expired API Key]"
        return f"❌ HTTP Error ({e.code})"
    except Exception as e:
        return f"❌ Lookup Failed [{str(e)}]"


def parse_authentication_headers(msg):
    """Surgically extracts SPF, DKIM, and DMARC verification states from email headers."""
    spf_status = "NOT FOUND"
    dkim_status = "NOT FOUND"
    dmarc_status = "NOT FOUND"
    
    auth_headers = msg.get_all('Authentication-Results', []) or []
    for header in auth_headers:
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

    if spf_status == "NOT FOUND":
        received_spf = msg.get_all('Received-SPF', []) or []
        for header in received_spf:
            header_clean = header.lower()
            if 'pass' in header_clean: spf_status = "PASS"
            elif 'fail' in header_clean: spf_status = "FAIL"
            elif 'softfail' in header_clean: spf_status = "SOFTFAIL"
            elif 'neutral' in header_clean: spf_status = "NEUTRAL"
            if spf_status != "NOT FOUND": break

    def get_status_icon(status):
        if status == "PASS": return f"✅ {status}"
        if status in ["FAIL", "HARDFAIL"]: return f"❌ {status} [HIGH RISK]"
        if status in ["SOFTFAIL", "NEUTRAL", "NONE"]: return f"⚠️ {status} [UNVERIFIED]"
        return f"❔ {status}"

    print("--- 🔐 PROTOCOL AUTHENTICATION CHECKS ---")
    print(f" 🛡️  SPF (Sender Policy Framework):     {get_status_icon(spf_status)}")
    print(f" 🛡️  DKIM (DomainKeys Identified Mail):  {get_status_icon(dkim_status)}")
    print(f" 🛡️  DMARC (Domain Authentication Policy): {get_status_icon(dmarc_status)}\n")
    
    return {"spf": spf_status, "dkim": dkim_status, "dmarc": dmarc_status}


def run_gemini_cognitive_analysis(subject, sender, body, auth_results, vt_results):
    """Dispatches full analytical context to Gemini for defensive intent processing."""
    print("--- 🧠 AI COGNITIVE THREAT ANALYSIS ---")
    print("[*] Dispatching telemetric payloads to Google Gemini Cloud Engine...")

    if not GEMINI_API_KEY or "INPUT YOUR" in GEMINI_API_KEY or GEMINI_API_KEY.strip() == "":
        print("⚠️ Skipped [Gemini API Key Missing]")
        return

    system_prompt = (
        "You are an elite Tier 3 SOC incident responder, digital forensics specialist, and defensive architect. "
        "Analyze the provided email elements for underlying social engineering schemes, architectural risk, "
        "obfuscation tricks, and compliance violations. Your output must be highly professional, structured, and descriptive. "
        "Do not use markdown blocks or code formatting backticks. Output exactly these titled headers:\n"
        "1. PSYCHOLOGICAL ANALYSIS (Examine use of urgency, intimidation, authority spoofing, or greed manipulation)\n"
        "2. INFRASRUCTURE ANOMALY DETECTION (Evaluate domain mismatches, cross-referencing failed headers against routing traces)\n"
        "3. INTENT-BASED SOC RISK RATING (Provide a final assessment: CRITICAL, HIGH, MEDIUM, or LOW, with technical justification)\n"
        "4. TACTICAL INCIDENT REMEDIATION PLAN (List exact steps for the security engineering team to contain and harden the environment)"
    )

    context_payload = (
        f"Subject Line: {subject}\n"
        f"Sender: {sender}\n"
        f"Extracted Email Body:\n{body}\n\n"
        f"Authentication States: SPF={auth_results['spf']}, DKIM={auth_results['dkim']}, DMARC={auth_results['dmarc']}\n"
        f"VirusTotal OSINT Reputation Results: {json.dumps(vt_results)}"
    )

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=context_payload,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.15
            )
        )
        print(f"\n{response.text.strip()}\n")
    except Exception as e:
        print(f"❌ Gemini Incident Engine Processing Error: {str(e)}\n")


def analyze_phishing_email(raw_email):
    """Parses and analyzes the raw email content for security risks."""
    msg = message_from_string(raw_email)
    
    subject = msg.get('Subject', '[NO SUBJECT FOUND]')
    sender = msg.get('From', '[NO SENDER FOUND]')
    recipient = msg.get('To', '[NO RECIPIENT FOUND]')
    
    print("\n" + "=" * 25 + " [🚨 SOC AI-POWERED PHISHING REPORT] " + "=" * 25)
    print(f"🔹 Subject:   {subject}")
    print(f"🔹 From:      {sender}")
    print(f"🔹 To:        {recipient}")
    
    source_ip = msg.get('X-Sender-IP')
    if not source_ip:
        received_headers = msg.get_all('Received', []) or []
        for header in received_headers:
            ip_match = re.search(r'\[([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\]', header)
            if ip_match:
                source_ip = f"{ip_match.group(1)} (Extracted via Received Path)"
                break
    print(f"🔹 Source IP: {source_ip or 'Unknown / Cloud Routed'}\n")
    
    # Run Technical Infrastructure Verification Layers
    auth_results = parse_authentication_headers(msg)
    
    # Extract Email Content Body
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
            
    # Extract Target Hyperlinks
    links = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', body) + re.findall(r'(https?://[^\s<>"\']+)', body)))
    
    print("--- 🔗 EXTRACTED LINKS FOR TRIAGE & REPUTATION CHECK ---")
    vt_tracker = {}
    if links:
        for idx, url in enumerate(links, 1):
            print(f" [{idx}] -> {url}")
            vt_status = check_virustotal(url, VIRUSTOTAL_API_KEY)
            print(f"      ↳ 🛡️ VirusTotal: {vt_status}\n")
            vt_tracker[url] = vt_status
    else:
        print("[*] No active hyperlinks found in the email body.\n")
        
    # Execute Cognitive Layer Processing Handoff
    run_gemini_cognitive_analysis(subject, sender, body, auth_results, vt_tracker)
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
    target_file_path = find_the_email_file(SCRIPT_DIR)
    
    if not target_file_path:
        default_path = os.path.join(SCRIPT_DIR, "email_to_analyze.txt")
        with open(default_path, "w", encoding="utf-8") as f:
            f.write("DELETE THIS LINE AND PASTE YOUR RAW EMAIL TEXT HERE")
            
        print(f"[!] Target email file was missing. Created template at:")
        print(f"    -> {default_path}")
        print("\n[🎯 ACTION REQUIRED]: Open 'email_to_analyze.txt', paste raw email headers/content, save, and run.")
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
