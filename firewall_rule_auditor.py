import requests

def audit_firewall(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
        
    print(f"\n--- [ Firewall/Security Rule Auditor: {url} ] ---")
    
    try:
        # Request with headers to mimic a browser
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, timeout=10, headers=headers)
        
        # Security Header Analysis
        security_headers = ['Server', 'X-Powered-By', 'X-AspNet-Version']
        found_headers = {h: response.headers.get(h, 'Not Found') for h in security_headers}
        
        print("[+] Header Analysis:")
        for h, v in found_headers.items():
            print(f"    - {h}: {v}")
            
        # Firewall Detection Logic
        server_info = response.headers.get('Server', '').lower()
        if 'cloudflare' in server_info or 'cf-ray' in response.headers:
            print("\n[!] FIREWALL DETECTED: Cloudflare is active (WAF).")
        elif 'awselb' in server_info:
            print("\n[!] FIREWALL DETECTED: AWS Load Balancer/WAF active.")
        else:
            print("\n[-] NO WAF DETECTED: The server might be directly exposed.")
            print("    [!] Warning: This is risky, direct IP access might be possible.")

    except Exception as e:
        print(f"[!] Audit Error: {e}")

if __name__ == "__main__":
    target = input("Audit karne ke liye URL: ")
    audit_firewall(target)