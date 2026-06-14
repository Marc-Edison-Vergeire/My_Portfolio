import time
import concurrent.futures
import requests
import re
import socket
from urllib.parse import urlparse

# ==========================================
# CONFIGURATION & API KEYS
# ==========================================
URLSCAN_API_KEY = "019e8819-090c-765e-94ea-72f59ba7ab22"
VIRUSTOTAL_API_KEY = "f4786ae4d1cf33e451d040b9441d9a7682ca83ec69efb6d4f5cd6d2372fbf1a9"

HEADERS_VT = {
    "accept": "application/json",
    "x-apikey": VIRUSTOTAL_API_KEY
}

HEADERS_URLSCAN = {
    "API-Key": URLSCAN_API_KEY,
    "Content-Type": "application/json"
}

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def defang(observable):
    """Defangs URLs and IPs to prevent accidental clicking in incident logs."""
    if not observable or not isinstance(observable, str):
        return "N/A"
    text = observable.replace("http://", "hxxp://").replace("https://", "hxxps://")
    text = re.sub(r'\.(?!$)', '[.]', text)
    text = text.replace("://", "[://]")
    return text

def extract_domain(url_string):
    """Safely parses out the bare domain or host string from any target input."""
    if not url_string.startswith(('http://', 'https://')):
        url_string = 'http://' + url_string
    try:
        parsed_url = urlparse(url_string)
        return parsed_url.hostname
    except Exception:
        return None

def resolve_url_to_ip(domain):
    """Resolves a plain domain string to an active IPv4."""
    if not domain:
        return None
    try:
        return socket.gethostbyname(domain)
    except Exception:
        return None

# ==========================================
# ZERO-INSTALLATION ENRICHMENT ENGINES (API-Based)
# ==========================================

def get_dns_records_via_api(domain):
    """Queries Cloudflare's DNS-over-HTTPS API to fetch MX and NS records without dependencies."""
    if not domain or re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", domain):
        return {"status": "Skipped (DNS routing maps apply to URLs/Domains only)"}
    
    headers = {"accept": "application/dns-json"}
    records = {"mx": [], "ns": []}
    
    try:
        # Fetch Mail Exchanger (MX) Records (Type 15)
        mx_res = requests.get(f"https://cloudflare-dns.com/dns-query?name={domain}&type=MX", headers=headers, timeout=8)
        if mx_res.status_code == 200:
            answers = mx_res.json().get("Answer", [])
            for ans in answers:
                records["mx"].append(ans.get("data"))
        
        # Fetch Nameserver (NS) Records (Type 2)
        ns_res = requests.get(f"https://cloudflare-dns.com/dns-query?name={domain}&type=NS", headers=headers, timeout=8)
        if ns_res.status_code == 200:
            answers = ns_res.json().get("Answer", [])
            for ans in answers:
                records["ns"].append(ans.get("data"))
                
    except Exception as e:
        return {"error": f"DNS API Error: {str(e)}"}
        
    if not records["mx"]: records["mx"] = ["None detected / Unconfigured"]
    if not records["ns"]: records["ns"] = ["None detected"]
    return records


def get_whois_via_rdap(domain):
    """Queries open RDAP gateways to extract registrar details and domain creation tracking data."""
    if not domain or re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", domain):
        return {"status": "Skipped (Whois records apply to Domains only)"}
    
    try:
        # Request data from standard registration registry framework redirection engine
        url = f"https://rdap.org/domain/{domain}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract Registrar
            registrar = "Unknown / Private"
            entities = data.get("entities", [])
            for entity in entities:
                if "registrar" in entity.get("roles", []):
                    vcard = entity.get("vcardArray", [None, []])[1]
                    for entry in vcard:
                        if entry[0] == "fn":
                            registrar = entry[3]
                            break

            # Extract Dates from events timelines
            created_date = "N/A"
            expiry_date = "N/A"
            events = data.get("events", [])
            for event in events:
                if event.get("eventAction") == "registration":
                    created_date = event.get("eventDate", "N/A")[:10] # Grab YYYY-MM-DD
                elif event.get("eventAction") == "expiration":
                    expiry_date = event.get("eventDate", "N/A")[:10]

            return {
                "registrar": registrar,
                "creation_date": created_date,
                "expiration_date": expiry_date,
                "country": data.get("port43", "N/A").split("\n")[-1] or "N/A" # Fallback mapping
            }
        return {"error": f"RDAP data unavailable (HTTP {response.status_code})"}
    except Exception as e:
        return {"error": f"RDAP Tracking Error: {str(e)}"}


def get_network_geolocation(ip_address):
    """Queries ip-api.com to fetch BGP ASN and ISP network infrastructure context."""
    if not ip_address:
        return {"error": "No IP available"}
    try:
        url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,isp,as,org"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            res_data = response.json()
            if res_data.get("status") == "success":
                return {
                    "country": res_data.get("country"),
                    "region": res_data.get("regionName"),
                    "isp": res_data.get("isp"),
                    "org": res_data.get("org"),
                    "asn": res_data.get("as")
                }
        return {"error": "Failed to fetch geolocation maps"}
    except Exception as e:
        return {"error": str(e)}

# ==========================================
# SCANNER FUNCTIONS (Authenticated)
# ==========================================

def scan_virustotal(observable, obs_type="url"):
    try:
        if obs_type == "url":
            import base64
            url_id = base64.urlsafe_b64encode(observable.encode()).decode().strip("=")
            endpoint = f"https://www.virustotal.com/api/v3/urls/{url_id}"
        elif obs_type == "ip":
            endpoint = f"https://www.virustotal.com/api/v3/ip_addresses/{observable}"
        else:
            return {"error": "Invalid input type"}

        response = requests.get(endpoint, headers=HEADERS_VT, timeout=15)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("attributes", {})
            stats = data.get("last_analysis_stats", {})
            return {
                "malicious": stats.get("malicious", 0),
                "suspicious": stats.get("suspicious", 0),
                "harmless": stats.get("harmless", 0),
                "reputation": data.get("reputation", 0)
            }
        elif response.status_code == 404:
            return {"status": "No historical record found (Clean/Unscanned)"}
        else:
            return {"error": f"HTTP Error {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def scan_urlscan(observable, obs_type="url"):
    try:
        if obs_type == "url":
            payload = {"url": observable, "visibility": "public"}
            submit_url = "https://urlscan.io/api/v1/scan/"
            submit_res = requests.post(submit_url, headers=HEADERS_URLSCAN, json=payload, timeout=15)
            if submit_res.status_code != 200:
                return {"error": "Scan submission failed"}
                
            result_api_url = submit_res.json().get("api")
            for _ in range(12):
                time.sleep(5)
                res = requests.get(result_api_url, headers=HEADERS_URLSCAN, timeout=15)
                if res.status_code == 200:
                    data = res.json()
                    verdicts = data.get("verdicts", {}).get("overall", {})
                    return {
                        "score": verdicts.get("score", 0),
                        "malicious": verdicts.get("malicious", False),
                        "categories": verdicts.get("tags", []),
                        "screenshot": data.get("task", {}).get("screenshotURL", "N/A")
                    }
            return {"status": "Analysis timeout on engine"}
        elif obs_type == "ip":
            endpoint = f"https://urlscan.io/api/v1/search/?q=ip:{observable}"
            res = requests.get(endpoint, headers=HEADERS_URLSCAN, timeout=15)
            if res.status_code == 200:
                results = res.json().get("results", [])
                return {
                    "historical_hits": len(results),
                    "latest_match": results[0].get("task", {}).get("url") if results else "None"
                }
            return {"error": "Search endpoint error"}
    except Exception as e:
        return {"error": str(e)}

def scan_urlhaus(observable, obs_type="url"):
    if obs_type != "url":
        return {"status": "Skipped (URLhaus tracks URLs/Domains only)"}
    url = "https://urlhaus-api.abuse.ch/v1/url/"
    try:
        response = requests.post(url, data={'url': observable}, timeout=10)
        if response.status_code == 200:
            res_data = response.json()
            if res_data.get("query_status") == "ok":
                return {
                    "listed": True,
                    "status": res_data.get("url_status"),
                    "threat": res_data.get("threat"),
                    "tags": res_data.get("tags", [])
                }
            return {"listed": False, "status": "Clean / Not listed"}
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def scan_threatfox(observable, obs_type="ip"):
    url = "https://threatfox-api.abuse.ch/api/v1/"
    payload = {"query": "search_ioc", "search_term": observable}
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            res_data = response.json()
            if res_data.get("query_status") == "ok":
                ioc_match = res_data.get("data", [{}])[0]
                return {
                    "listed": True,
                    "threat_type": ioc_match.get("threat_type"),
                    "malware": ioc_match.get("malware_printable"),
                    "confidence": ioc_match.get("confidence_level")
                }
            return {"listed": False, "status": "Clean / Not listed"}
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def check_spamhaus_dnsbl(observable, obs_type="ip"):
    if obs_type != "ip":
        return {"status": "Skipped (DNSBL evaluations apply to IPs only)"}
    try:
        reversed_ip = ".".join(reversed(observable.split(".")))
        query_domain = f"{reversed_ip}.zen.spamhaus.org"
        resolved_address = socket.gethostbyname(query_domain)
        if resolved_address.startswith("127.0."):
            return {"listed": True, "return_code": resolved_address}
    except socket.gaierror:
        return {"listed": False, "status": "Clean / Not listed"}
    except Exception as e:
        return {"error": str(e)}

# ==========================================
# REPORT FORMATTING ENGINE
# ==========================================

def generate_formal_report(observable, obs_type, resolved_ip, target_domain, geo, dns_data, whois_data, vt, us, uh, tf, sh):
    defanged_obs = defang(observable)
    defanged_ip = defang(resolved_ip) if resolved_ip else "N/A"
    
    # Calculate posture matrix
    vt_m = vt.get("malicious", 0) if isinstance(vt, dict) else 0
    us_m = us.get("malicious", False) if isinstance(us, dict) else False
    uh_l = uh.get("listed", False) if isinstance(uh, dict) else False
    tf_l = tf.get("listed", False) if isinstance(tf, dict) else False
    sh_l = sh.get("listed", False) if isinstance(sh, dict) else False

    if vt_m > 5 or us_m or uh_l or tf_l or sh_l:
        severity = "CRITICAL / CONFIRMED MALICIOUS"
    elif vt_m > 0 or (isinstance(us, dict) and us.get("score", 0) > 40):
        severity = "SUSPICIOUS / INVESTIGATION MANDATORY"
    else:
        severity = "LOW RISK / INFORMATIONAL"

    print("\n" + "="*75)
    print("                 SOC AUTOMATED SYSTEM MULTI-SCANNER REPORT                ")
    print("="*75)
    print(f"INDICATOR UNDER REVIEW : {defanged_obs}")
    print(f"OBSERVABLE TYPE        : {obs_type.upper()}")
    print(f"RESOLVED HOST IP       : {defanged_ip}")
    print(f"ASSESSED RISK POSTURE  : {severity}")
    print("-" * 75)
    
    # WHOIS API RECORD DISPLAY
    print("[+] DOMAIN IDENTIFICATION & METADATA (RDAP API)")
    if "status" in whois_data:
        print(f"    Status: {whois_data['status']}")
    elif "error" in whois_data:
        print(f"    Status: {whois_data['error']}")
    else:
        print(f"    Registrar Vendor   : {whois_data.get('registrar')}")
        print(f"    Creation Timestamp : {whois_data.get('creation_date')}")
        print(f"    Registry Expiry    : {whois_data.get('expiration_date')}")
    print("-" * 75)

    # PASSIVE DNS API DISPLAY
    print("[+] PASSIVE DNS INTERACTION DATA (DOH API)")
    if "status" in dns_data:
        print(f"    Status: {dns_data['status']}")
    elif "error" in dns_data:
        print(f"    Status: {dns_data['error']}")
    else:
        print(f"    Active Nameservers : {', '.join(dns_data.get('ns', []))}")
        print(f"    Mail Exchange (MX) : {', '.join(dns_data.get('mx', []))}")
    print("-" * 75)

    # GEOLOCATION DISPLAY
    print("[+] NETWORK INFRASTRUCTURE ENRICHMENT")
    if not geo or "error" in geo:
        print(f"    Status: Data unavailable or endpoint timed out.")
    else:
        print(f"    Geographic Country : {geo.get('country')}")
        print(f"    Geographic Region  : {geo.get('region')}")
        print(f"    Infrastructure ISP : {geo.get('isp')}")
        print(f"    ASN Number/Routing : {geo.get('asn')}")
        print(f"    Organization Group : {geo.get('org')}")
    print("-" * 75)
    
    # 1. VIRUSTOTAL
    print("[+] SECTION 1: VIRUSTOTAL REPUTATION MATRIX")
    if "error" in vt: print(f"    Status: ERROR - {vt['error']}")
    elif "status" in vt: print(f"    Status: {vt['status']}")
    else:
        print(f"    Malicious Flags    : {vt['malicious']} vendors")
        print(f"    Suspicious Flags   : {vt['suspicious']} vendors")
        print(f"    Community Score    : {vt['reputation']}")
    print("-" * 75)

    # 2. URLSCAN.IO
    print("[+] SECTION 2: URLSCAN.IO BEHAVIORAL DISCOVERY")
    if "error" in us: print(f"    Status: ERROR - {us['error']}")
    elif "status" in us: print(f"    Status: {us['status']}")
    else:
        if obs_type == "url":
            print(f"    Computed Risk Score: {us['score']}/100")
            print(f"    Categorized Tags   : {', '.join(us['categories']) if us['categories'] else 'None'}")
            print(f"    Interactive Capture: {us['screenshot']}")
        else:
            print(f"    Historical Sighting: {us['historical_hits']} events recorded")
            print(f"    Context Reference  : {defang(us['latest_match'])}")
    print("-" * 75)

    # 3. URLHAUS
    print("[+] SECTION 3: URLHAUS OPEN-SOURCE INTEL (KEYLESS)")
    if "error" in uh: print(f"    Status: ERROR - {uh['error']}")
    else:
        print(f"    Threat Database Hit: {uh.get('listed', False)}")
        if uh.get("listed"):
            print(f"    Payload Host Status: {uh.get('status')}")
            print(f"    Malware Assignment : {uh.get('threat')}")
            print(f"    Associated Tags    : {', '.join(uh.get('tags', []))}")
    print("-" * 75)

    # 4. THREATFOX
    print("[+] SECTION 4: THREATFOX BOTNET INFRASTRUCTURE FEED (KEYLESS)")
    if "error" in tf: print(f"    Status: ERROR - {tf['error']}")
    else:
        print(f"    C2 Infrastructure Match: {tf.get('listed', False)}")
        if tf.get("listed"):
            print(f"    IoC Variant Profile    : {tf.get('threat_type')}")
            print(f"    Assigned Target Family : {tf.get('malware')}")
            print(f"    Confidence Index Score : {tf.get('confidence')}%")
    print("-" * 75)

    # 5. SPAMHAUS DNSBL
    print("[+] SECTION 5: SPAMHAUS REAL-TIME REPUTATION ZONE (KEYLESS)")
    if "error" in sh: print(f"    Status: ERROR - {sh['error']}")
    elif obs_type != "ip" and not resolved_ip: print(f"    Status: {sh.get('status')}")
    else:
        print(f"    Identified on Blocklist: {sh.get('listed', False)}")
        if sh.get("listed"):
            print(f"    Zone Resolution Vector : {sh.get('return_code')} (Spam/Malware/Botnet Egress)")
    print("="*75)

# ==========================================
# ORCHESTRATOR
# ==========================================

if __name__ == "__main__":
    print("[*] Launching SOC Multi-Engine Stream...")
    user_input = input("Enter target tracking artifact (URL or IP): ").strip()
    
    if any(char.isalpha() for char in user_input) and "." in user_input:
        observable_type = "url"
        target_domain = extract_domain(user_input)
        target_ip = resolve_url_to_ip(target_domain)
    else:
        observable_type = "ip"
        target_domain = None
        target_ip = user_input
        
    print(f"[*] Target IP Location Vector mapped: {target_ip if target_ip else 'Could not resolve domain IP'}")
    print(f"[*] Dispatching background queries across 8 keyless & authenticated layers...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_vt = executor.submit(scan_virustotal, user_input, observable_type)
        future_us = executor.submit(scan_urlscan, user_input, observable_type)
        future_uh = executor.submit(scan_urlhaus, user_input, observable_type)
        
        # Parallel Enrichment (Pure API Tracks)
        future_whois = executor.submit(get_whois_via_rdap, target_domain)
        future_dns = executor.submit(get_dns_records_via_api, target_domain)
        future_geo = executor.submit(get_network_geolocation, target_ip)
        
        # IP Intelligence
        future_tf = executor.submit(scan_threatfox, target_ip if target_ip else user_input, "ip")
        future_sh = executor.submit(check_spamhaus_dnsbl, target_ip if target_ip else user_input, "ip")
        
        # Collate
        vt_res = future_vt.result()
        us_res = future_us.result()
        uh_res = future_uh.result()
        whois_res = future_whois.result()
        dns_res = future_dns.result()
        geo_res = future_geo.result()
        tf_res = future_tf.result()
        sh_res = future_sh.result()
        
    generate_formal_report(
        user_input, observable_type, target_ip, target_domain,
        geo_res, dns_res, whois_res, vt_res, us_res, uh_res, tf_res, sh_res
    )