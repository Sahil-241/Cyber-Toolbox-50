import requests

def full_audit(url):
    if not url.startswith("http"): url = "http://" + url
    
    print(f"\n--- [ Starting Full Security Audit: {url} ] ---")
    
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        html = response.text.lower()
        
        # 1. Tech Stack Detection
        server = headers.get('Server', 'Unknown')
        x_powered = headers.get('X-Powered-By', 'Not Specified')
        print(f"[+] Server: {server} | Tech: {x_powered}")
        
        # 2. CMS & Vulnerability Database
        cms_db = {
            'WordPress': {'sig': 'wp-content', 'risk': 'High', 'sol': 'Update plugins/themes.'},
            'Joomla': {'sig': 'joomla', 'risk': 'Medium', 'sol': 'Update Joomla core.'},
            'Drupal': {'sig': 'drupal.js', 'risk': 'Medium', 'sol': 'Apply security patches.'}
        }
        
        found = False
        for cms, info in cms_db.items():
            if info['sig'] in html:
                print(f"\n[!] CMS DETECTED: {cms}")
                print(f"    -> Risk Level: {info['risk']}")
                print(f"    -> Action: {info['sol']}")
                found = True
        
        if not found:
            print("\n[-] CMS Not Detected. This is a Custom/Hardened Site.")
            print("[+] Suggestion: Check for hidden files (Directory Brute-forcing).")

    except Exception as e:
        print(f"[!] Scan Error: {e}")

if __name__ == "__main__":
    target = input("Website URL: ")
    full_audit(target)