ascii="""
   _____ ____  ______    ___                __           __    ______            __
  / ___// __ \/ ____/   /   |  ____  ____ _/ /_  _______/ /_  /_  __/___  ____  / /
  \__ \/ / / / /       / /| | / __ \/ __ `/ / / / / ___/ __/   / / / __ \/ __ \/ / 
 ___/ / /_/ / /___    / ___ |/ / / / /_/ / / /_/ (__  ) /_    / / / /_/ / /_/ / /  
/____/\____/\____/   /_/  |_/_/ /_/\__,_/_/\__, /____/\__/   /_/  \____/\____/_/   
                                         /____/                                 

                              by Marc Edison Vergeire
                                       2026
"""
print(ascii)

import re
import os
from email import message_from_string
from datetime import datetime, timezone

class MHAEngine:
    def __init__(self, raw_headers_str):
        self.msg = message_from_string(raw_headers_str)
        self.summary_keys = [
            "subject", "from", "to", "cc", "date", "message-id", "return-path", 
            "reply-to", "sender", "delivered-to", "received-spf", "authentication-results"
        ]
        
    def get_basic_metadata(self):
        return {
            "Subject": self.msg.get("Subject", "N/A"),
            "From": self.msg.get("From", "N/A"),
            "To": self.msg.get("To", "N/A"),
            "Cc": self.msg.get("Cc", "N/A"),
            "Date": self.msg.get("Date", "N/A"),
            "Message-ID": self.msg.get("Message-ID", "N/A"),
            "Return-Path": self.msg.get("Return-Path", "N/A"),
            "Reply-To": self.msg.get("Reply-To", "N/A"),
            "Sender": self.msg.get("Sender", "N/A"),
            "Delivered-To": self.msg.get("Delivered-To", "N/A"),
            "Received-SPF": self.msg.get("Received-SPF", "N/A")
        }

    def parse_authentication_results(self):
        auth_header = self.msg.get("Authentication-Results", "")
        results = {"spf": "NONE", "dkim": "NONE", "dmarc": "NONE", "raw": auth_header}
        if not auth_header:
            return results
        auth_clean = " ".join(auth_header.split())
        for protocol in ["spf", "dkim", "dmarc"]:
            match = re.search(r'\b' + protocol + r'=([a-zA-Z]+)', auth_clean, re.IGNORECASE)
            if match:
                results[protocol] = match.group(1).upper()
        return results

    def parse_hops_timeline(self):
        received_headers = self.msg.get_all("Received", []) or []
        hops = []
        if not received_headers:
            return hops

        for idx, raw_hop in enumerate(reversed(received_headers)):
            hop_clean = " ".join(raw_hop.split())
            timestamp = None
            dt_obj = None
            
            if ";" in hop_clean:
                time_str = hop_clean.split(";")[-1].strip()
                time_str = re.sub(r'\s*\([^)]+\)$', '', time_str) 
                formats = ["%a, %d %b %Y %H:%M:%S %z", "%d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z", "%d %b %Y %H:%M:%S"]
                for fmt in formats:
                    try:
                        parsed_dt = datetime.strptime(time_str, fmt)
                        if parsed_dt.tzinfo is not None:
                            dt_obj = parsed_dt.astimezone(timezone.utc).replace(tzinfo=None)
                        else:
                            dt_obj = parsed_dt
                        timestamp = parsed_dt.strftime("%Y-%m-%d %H:%M:%S")
                        if parsed_dt.tzinfo:
                            timestamp += f" {parsed_dt.strftime('%z')}"
                        break
                    except ValueError:
                        continue

            from_match = re.search(r'from\s+([^\s]+)', hop_clean, re.IGNORECASE)
            by_match = re.search(r'by\s+([^\s]+)', hop_clean, re.IGNORECASE)
            ip_match = re.search(r'\[([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\]', hop_clean)

            submitting_host = from_match.group(1) if from_match else "Unknown"
            receiving_host = by_match.group(1) if by_match else "Unknown"
            source_ip = ip_match.group(1) if ip_match else "N/A"

            delay = 0
            if idx > 0 and dt_obj and hops[idx-1]['_dt_obj']:
                prev_dt = hops[idx-1]['_dt_obj']
                diff_seconds = int((dt_obj - prev_dt).total_seconds())
                delay = max(0, diff_seconds)

            hops.append({
                "hop": idx + 1,
                "from": submitting_host,
                "by": receiving_host,
                "ip": source_ip,
                "time": timestamp or "Unknown Time",
                "delay_sec": delay,
                "_dt_obj": dt_obj 
            })
        return hops

    def get_specific_categories(self):
        categories = {
            "AUTHENTICATION SIGNATURES": ["ARC-Seal", "ARC-Message-Signature", "ARC-Authentication-Results", "DKIM-Signature"],
            "MAILGUN INFRASTRUCTURE": ["X-Mailgun-Sid", "X-Feedback-Id", "X-Mailgun-Sending-Ip-Pool-Name", "X-Mailgun-Sending-Ip-Pool", "X-Mailgun-Sending-Ip", "X-Mailgun-Tag", "X-Mailgun-Variables", "Feedback-Id"],
            "MICROSOFT & ABUSE FILTERS": ["X-Microsoft-Antispam-Mailbox-Delivery", "List-Unsubscribe-Post", "Mailing_list_unsubscribe_url", "List-Unsubscribe"],
            "INTERNAL GOOGLE/PROVIDER HOPS": ["X-Received"],
            "CONTENT MECHANICS": ["Mime-Version", "Content-Type"]
        }
        extracted_data = {}
        for cat_name, keys in categories.items():
            cat_dict = {}
            for key in keys:
                values = self.msg.get_all(key)
                if values:
                    cat_dict[key] = [" ".join(v.split()) for v in values]
            if cat_dict:
                extracted_data[cat_name] = cat_dict
        return extracted_data

    def get_remaining_headers(self):
        all_known_keys = set(self.summary_keys)
        explicit_categories_keys = [
            "arc-seal", "arc-message-signature", "arc-authentication-results", "dkim-signature",
            "x-mailgun-sid", "x-feedback-id", "x-mailgun-sending-ip-pool-name", "x-mailgun-sending-ip-pool", 
            "x-mailgun-sending-ip", "x-mailgun-tag", "x-mailgun-variables", "feedback-id",
            "x-microsoft-antispam-mailbox-delivery", "list-unsubscribe-post", "mailing_list_unsubscribe_url", 
            "list-unsubscribe", "mime-version", "content-type", "x-received"
        ]
        for k in explicit_categories_keys:
            all_known_keys.add(k)
        remains = {}
        for key in self.msg.keys():
            if key.lower() not in all_known_keys:
                values = self.msg.get_all(key)
                if values:
                    remains[key] = [" ".join(v.split()) for v in values]
        return dict(sorted(remains.items()))

def bold_text(text):
    """Helper function to bold text dynamically without polluting code strings."""
    return f"\033[1m{text}\033[0m"

def print_full_value(key, values):
    # Dynamically injects bold tags strictly inside the left header layout block
    bold_key = bold_text(f"{key:<28}")
    empty_prefix = f" {'':<28} | "
    for val_idx, val in enumerate(values):
        prefix = f" {bold_key} | " if val_idx == 0 else empty_prefix
        print(f"{prefix}{val}")

def render_mha_report(analyzer):
    meta = analyzer.get_basic_metadata()
    auth = analyzer.parse_authentication_results()
    hops = analyzer.parse_hops_timeline()
    categories = analyzer.get_specific_categories()
    remains = analyzer.get_remaining_headers()

    LINE_LEN = 78
    print("=" * LINE_LEN)
    print(f" {bold_text('PHISHOPS MAIL HEADER ANALYZER - COMPLETE REPORT'):^{LINE_LEN + 8}} ")
    print("=" * LINE_LEN)
    
    print(f"\n{bold_text('[+] SUMMARY / ENVELOPE METADATA')}")
    print("-" * 40)
    for k, v in meta.items():
        print(f" {bold_text(f'{k:<15}')}: {v}")

    print(f"\n{bold_text('[+] SECURITY GATEKEEPER ANALYSIS')}")
    print("-" * 40)
    for protocol in ['spf', 'dkim', 'dmarc']:
        status = auth[protocol]
        alert = " [!] FAIL / EXPLOIT RISK" if status == "FAIL" else ""
        print(f" {bold_text(f'{protocol.upper():<10}')}: {status}{alert}")
        
    from_header = meta['From']
    return_path_raw = meta['Return-Path']
    if "@" in from_header:
        from_domain = from_header.split('@')[-1].replace('>', '').strip()
        if return_path_raw and "@" in return_path_raw:
            return_domain = return_path_raw.split('@')[-1].replace('>', '').strip()
            if from_domain.lower() != return_domain.lower():
                print(f"\n{bold_text('[CRITICAL WARNING] Mismatched Domains Detected!')}")
                print(f"   -> Visible Sender Claims Domain: {from_domain}")
                print(f"   -> Actual Return/Bounce Path : {return_domain}")

    print(f"\n{bold_text('[+] SERVER ROUTING HOP TIMELINE')}")
    print("-" * LINE_LEN)
    print(f"{bold_text('HOP'):<11} | {bold_text('SUBMITTING (FROM)'):<33} | {bold_text('RECEIVING (BY)'):<33} | {bold_text('DELAY')}")
    print("-" * LINE_LEN)
    for hop in hops:
        delay_str = f"+{hop['delay_sec']}s" if hop['delay_sec'] > 0 else "0s"
        from_host = (hop['from'][:22] + "...") if len(hop['from']) > 25 else hop['from']
        by_host = (hop['by'][:22] + "...") if len(hop['by']) > 25 else hop['by']
        print(f"{hop['hop']:<3} | {from_host:<25} | {by_host:<25} | {delay_str:<6}")
    print("-" * LINE_LEN)

    for cat_name, content in categories.items():
        print(f"\n{bold_text('[+] Category Matrix: ' + cat_name)}")
        print("=" * LINE_LEN)
        print(f"{bold_text('HEADER KEY'):<36} | {bold_text('VALUE(S) EXTRACTED')}")
        print("-" * LINE_LEN)
        for key, values in content.items():
            print_full_value(key, values)
        print("=" * LINE_LEN)

    if remains:
        print(f"\n{bold_text('[+] ADDITIONAL UNCLASSIFIED HEADERS')}")
        print("=" * LINE_LEN)
        for key, values in remains.items():
            print_full_value(key, values)
        print("=" * LINE_LEN)

if __name__ == "__main__":
    INPUT_FILE = "email_input.txt"
    
    print(f"[*] Engine Started. Searching for file: {os.path.abspath(INPUT_FILE)}")
    
    if not os.path.exists(INPUT_FILE):
        with open(INPUT_FILE, "w", encoding="utf-8") as template:
            template.write("=== PASTE RAW EMAIL OR HEADERS HERE ===")
        print(f"[!] '{INPUT_FILE}' was missing. Created it for you.")
        print("[>] Open 'email_input.txt', paste your email data, save it, and re-run.")
    else:
        with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
            raw_content = f.read().strip()
            
        print(f"[*] File loaded successfully. Size: {len(raw_content)} characters.")
        
        if len(raw_content) < 10:
            print("[-] Warning: The file 'email_input.txt' is practically empty! Please paste data inside it.")
        else:
            mha_app = MHAEngine(raw_content)
            render_mha_report(mha_app)
            print("\n[*] Execution completed successfully.")