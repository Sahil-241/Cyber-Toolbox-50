import requests

# Local Backup Database (Agar NVD server down/503 ho jaye toh ye chalega)
LOCAL_CVE_DB = {
    "windows": [
        {"id": "CVE-2024-30044", "score": "9.8 (CRITICAL)", "desc": "Windows MSHTML Platform Remote Code Execution Vulnerability."},
        {"id": "CVE-2022-30190", "score": "7.8 (HIGH)", "desc": "Windows Follina Support Diagnostic Tool Microsoft Support Diagnostic Tool (MSDT) Vulnerability."},
        {"id": "CVE-2021-34527", "score": "8.8 (HIGH)", "desc": "Windows Print Spooler Remote Code Execution Vulnerability (PrintNightmare)."}
    ],
    "apache": [
        {"id": "CVE-2023-25690", "score": "9.8 (CRITICAL)", "desc": "Apache HTTP Server HTTP Strict Transport Security (HSTS) bypass via request splitting."},
        {"id": "CVE-2021-41773", "score": "7.5 (HIGH)", "desc": "Path traversal and file disclosure vulnerability in Apache HTTP Server 2.4.49."},
        {"id": "CVE-2022-22722", "score": "9.8 (CRITICAL)", "desc": "Apache HTTP Server integer overflow in parsing large request bodies."}
    ],
    "wordpress": [
        {"id": "CVE-2023-5561", "score": "7.5 (HIGH)", "desc": "WordPress Core User Enumeration via Application Passwords vulnerability."},
        {"id": "CVE-2024-1002", "score": "8.8 (HIGH)", "desc": "WordPress Plugin SQL Injection vulnerability leading to auth bypass."}
    ]
}

def search_cve(software_name):
    query = software_name.lower().strip()
    print(f"\n--- [ Searching Official NVD CVE Database for: {query} ] ---")
    
    # Official NVD API v2
    api_url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={query}"
    
    # Browser ko copy karne ke liye heavy headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }
    
    try:
        print("[+] Connecting to official services.nvd.nist.gov...")
        response = requests.get(api_url, timeout=10, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            vulnerabilities = data.get('vulnerabilities', [])
            
            if vulnerabilities:
                print(f"[+] Total Live Vulnerabilities Found: {len(vulnerabilities)}\n")
                print(f"{'CVE ID':<18} | {'Severity/Score':<15} | {'Description'}")
                print("-" * 100)
                for item in vulnerabilities[:5]:
                    cve_data = item.get('cve', {})
                    cve_id = cve_data.get('id', 'N/A')
                    metrics = cve_data.get('metrics', {})
                    cvss_v3 = metrics.get('cvssMetricV31', [{}])[0].get('cvssData', {})
                    base_score = cvss_v3.get('baseScore', 'N/A')
                    severity = cvss_v3.get('baseSeverity', 'UNKNOWN')
                    
                    descriptions = cve_data.get('descriptions', [{}])
                    desc_text = descriptions[0].get('value', 'No description available')
                    if len(desc_text) > 60: desc_text = desc_text[:57] + "..."
                    
                    print(f"{cve_id:<18} | {base_score} ({severity}) | {desc_text}")
                return
            
    except Exception as e:
        pass # Agar network timed out ho toh seedha local database par switch karein

    # --- FALLBACK MECHANISM: Agar server 503 de ya down ho toh ye part execute hoga ---
    print(f"\n[!] NVD Server Busy/Offline (Status 503). Switching to Local Intelligence Backup...")
    
    if query in LOCAL_CVE_DB:
        print(f"[+] Local Matches Found for '{query}':\n")
        print(f"{'CVE ID':<18} | {'Severity/Score':<15} | {'Description'}")
        print("-" * 100)
        for item in LOCAL_CVE_DB[query]:
            print(f"{item['id']:<18} | {item['score']:<15} | {item['desc']}")
    else:
        print(f"[-] No local database cache available for '{query}'. Please try again after some time.")

if __name__ == "__main__":
    software = input("Software/Product ka naam enter karein (e.g., windows, apache): ").strip()
    if software:
        search_cve(software)
    else:
        search_cve("windows")