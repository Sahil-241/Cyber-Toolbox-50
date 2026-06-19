import requests
import ssl
import socket

def check_security(url):
    if not url.startswith("http"): url = "https://" + url
    score = 0
    total_checks = 7 
    
    # Header Mapping: (Risk Probability, Exploit Scenario, Solution)
    audit_data = {
        'Content-Security-Policy': ('90%', 'XSS/Injection: Malicious scripts run ho sakte hain.', 'Implement strict CSP policy.'),
        'X-Content-Type-Options': ('40%', 'MIME Sniffing: Malicious files ko executable ki tarah load karna.', 'Set X-Content-Type-Options: nosniff.'),
        'X-Frame-Options': ('85%', 'Clickjacking: User ko dhoke se button click karwana.', 'Set X-Frame-Options: SAMEORIGIN.'),
        'Strict-Transport-Security': ('75%', 'MITM Attack: User ka data intercept/chori karna.', 'Enable HSTS header.'),
        'X-XSS-Protection': ('50%', 'XSS Attack: Browser filter ko bypass karke data steal karna.', 'Set X-XSS-Protection: 1; mode=block.'),
        'Referrer-Policy': ('30%', 'Information Leakage: User ki private URL history leak hona.', 'Set Referrer-Policy: strict-origin.')
    }
    
    print(f"\n--- [ Security Scorecard for: {url} ] ---")
    
    # 1. SSL Check
    try:
        hostname = url.split("://")[-1].split("/")[0]
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print("[PASS] SSL/TLS Certificate: Valid")
                score += 1
    except:
        print("[FAIL] SSL/TLS Certificate: Invalid/Missing")

    # 2. Header & Vulnerability Check
    try:
        response = requests.get(url, timeout=10)
        print(f"[+] HTTP Status: {response.status_code}")
        
        for header, (prob, exploit, sol) in audit_data.items():
            if header in response.headers:
                print(f"[PASS] {header} Found.")
                score += 1
            else:
                print(f"\n[!] FAIL: {header} MISSING")
                print(f"    -> Hack Probability: {prob}")
                print(f"    -> How to Exploit: {exploit}")
                print(f"    -> Solution: {sol}")
                
    except Exception as e:
        print(f"[!] Connection Error: {e}")

    # 3. Final Scorecard
    percentage = (score / total_checks) * 100
    print("\n" + "="*50)
    print(f"FINAL SECURITY SCORE: {percentage:.2f}%")
    if percentage >= 80: print("Status: EXCELLENT - Highly Secure")
    elif percentage >= 50: print("Status: AVERAGE - Needs Patching")
    else: print("Status: INSECURE - High Risk of Exploitation!")
    print("="*50)

if __name__ == "__main__":
    target = input("Enter Website URL: ")
    check_security(target)