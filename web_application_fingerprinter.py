import requests
import re

def fingerprint_web_app(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
        
    print(f"\n--- [ Web Application Fingerprinter: {url} ] ---")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        print("[+] Sending request and analyzing application signatures...")
        response = requests.get(url, timeout=10, headers=headers)
        
        # 1. HTTP Headers Analysis
        server = response.headers.get('Server', 'Not Disclosed')
        powered_by = response.headers.get('X-Powered-By', 'Not Disclosed')
        backend_cookies = [cookie.name for cookie in response.cookies]
        
        print("\n[+] Component Analysis:")
        print(f"    - Web Server Infrastructure: {server}")
        print(f"    - Technology Stack Layer   : {powered_by}")
        
        # 2. Cookie Fingerprinting (Session identifier analysis)
        if backend_cookies:
            print(f"    - Active Session Cookies   : {', '.join(backend_cookies)}")
            for cookie in backend_cookies:
                if "PHPSESSID" in cookie:
                    print("      [!] Fingerprint Match: PHP Backend Engine Detected.")
                elif "JSESSIONID" in cookie:
                    print("      [!] Fingerprint Match: Java/Tomcat Application Server Detected.")
                elif "ASPSESSIONID" in cookie or "ASP.NET_SessionId" in cookie:
                    print("      [!] Fingerprint Match: Microsoft ASP.NET Infrastructure Detected.")
        
        # 3. HTML Source Signature Matching (Regex checks)
        html_content = response.text
        print("\n[+] Source Code Pattern Matching:")
        
        signatures = {
            "WordPress": r"/wp-content/|/wp-includes/",
            "Joomla": r"_joomla|Joomla!",
            "Drupal": r"Drupal\.settings",
            "Laravel": r"name=\"_token\"|X-CSRF-TOKEN",
            "React.js": r"data-reactroot|<div id=\"root\""
        }
        
        matched_any = False
        for app_name, pattern in signatures.items():
            if re.search(pattern, html_content, re.IGNORECASE):
                print(f"    [!] Framework Signatures: {app_name} deployment identified.")
                matched_any = True
                
        if not matched_any:
            print("    [-] Framework Signatures: No standard commercial CMS/Framework signature matched.")
            
    except Exception as e:
        print(f"[!] Fingerprinting Failed: {e}")

if __name__ == "__main__":
    target = input("Fingerprint karne ke liye URL daalein: ").strip()
    if target:
        fingerprint_web_app(target)
    else:
        print("[!] Input khali hai, test php web check kar rahe hain...")
        fingerprint_web_app("testphp.vulnweb.com")