import requests

def detect_and_test(target):
    # Protocol handle karna
    if not target.startswith(("http://", "https://")):
        url = "http://" + target
    else:
        url = target
        
    print(f"\n--- [ Scanning: {url} ] ---")
    
    try:
        response = requests.get(url, timeout=10)
        content_type = response.headers.get('Content-Type', '').lower()
        
        # Checking Status Code
        if response.status_code == 200:
            
            # Logic: Content-Type check karna
            if 'application/json' in content_type or 'application/xml' in content_type:
                print(f"[+] SUCCESS: API Detected at {url}")
                print(f"[!] Vulnerability Scan: API is publicly accessible!")
                print(f"[+] Data Snippet: {response.text[:200]}...")
                
            elif 'text/html' in content_type:
                print(f"[+] INFO: Normal Web Page Detected at {url}")
                print(f"[+] Status: 200 OK (Page is live, but it's not an API).")
                
            else:
                print(f"[+] INFO: Server responded with 200 OK (Unknown content type: {content_type})")
        
        elif response.status_code in [401, 403]:
            print(f"[+] SECURE: Endpoint is protected (Status: {response.status_code}).")
        else:
            print(f"[+] Server Response: {response.status_code}")

    except Exception as e:
        print(f"[!] Connection Error: {e}")

if __name__ == "__main__":
    target = input("URL enter karein: ")
    detect_and_test(target)