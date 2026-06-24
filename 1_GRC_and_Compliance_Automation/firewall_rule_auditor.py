import requests
import socket
import sys
import time

def audit_multi_layer_firewall(target):
    # URL Format Check
    url = target
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\n--- [ Project 50: Multi-Layer Security & Firewall Auditor ] ---")
    print(f"[+] Target Infrastructure : {url}")
    print("[+] Initiating Deep Network Layer Scanning...\n")
    time.sleep(1)

    try:
        # Resolve IP Address for Layer Analysis
        domain = url.replace("https://", "").replace("http://", "").split('/')[0]
        target_ip = socket.gethostbyname(domain)
        print(f"[+] Step 1: Resolved Domain IP -> {target_ip}")
    except Exception:
        print("[!] Error: Domain ya IP resolve nahi ho pa raha hai.")
        return

    layers_detected = 0
    detected_mechanisms = []

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, timeout=8, headers=headers)
        
        print("[*] Step 2: Analyzing Server Metadata & Return Hashes...")
        server_header = response.headers.get('Server', '').lower()
        
        # --- LAYER 1 DETECTION: CLOUD WAF SIGNATURES ---
        waf_signatures = {
            'cloudflare': 'Cloudflare Web Application Firewall',
            'cloudfront': 'AWS CloudFront / AWS WAF',
            'akamai': 'Akamai Edge Security / WAF',
            'sucuri': 'Sucuri CloudProxy',
            'imperva': 'Imperva Incapsula WAF'
        }
        
        found_waf = False
        for sig, name in waf_signatures.items():
            if sig in server_header or sig in str(response.headers).lower():
                detected_mechanisms.append(f"Layer {layers_detected + 1}: {name} (Edge Application Filter)")
                layers_detected += 1
                found_waf = True
                break
                
        if 'cf-ray' in response.headers or 'cf-cache-status' in response.headers:
            if not found_waf:
                detected_mechanisms.append("Layer 1: Cloudflare Traffic Proxy Shield")
                layers_detected += 1

        # --- LAYER 2 DETECTION: REVERSE PROXY / LOAD BALANCER ---
        # Agar Nginx, Apache ya Envoy peeche laga hai jo request forwarding kar raha hai
        proxy_headers = ['via', 'x-forwarded-for', 'x-forwarded-proto', 'forwarded']
        has_proxy_header = any(h in response.headers.get(h, '').lower() for h in proxy_headers)
        
        if has_proxy_header or any(p in server_header for p in ['nginx', 'envoy', 'haproxy']):
            detected_mechanisms.append(f"Layer {layers_detected + 1}: Reverse Proxy / Load Balancer Architecture")
            layers_detected += 1

        # --- LAYER 3 DETECTION: NETWORK SECURITY PROTOCOL CHECK ---
        # Custom or strict security policy responses indicating network-level dropping
        if response.status_code in [403, 502, 503] and not found_waf:
            detected_mechanisms.append(f"Layer {layers_detected + 1}: Gateway Access Control / Network IPS Filter")
            layers_detected += 1

        # --- FINAL OUTPUT PRINT BLOCK ---
        print("\n=================== [ FIREWALL ANALYSIS REPORT ] ===================")
        if layers_detected > 0:
            print(f"[+] STATUS          : PROTECTED (Firewall System Active)")
            print(f"[+] TOTAL LAYERS    : {layers_detected} Layer(s) Security Detected")
            print("\n[+] Detailed Infrastructure Mapping:")
            for mechanism in detected_mechanisms:
                print(f"    └── {mechanism}")
        else:
            print(f"[-] STATUS          : NO ACTIVE WAF LAYER DETECTED")
            print(f"[!] Warning         : Server direct public network par expose ho sakta hai.")
        print("====================================================================\n")

    except requests.exceptions.RequestException as e:
        print(f"[!] Scan Error: Connection drop ho gayi. Layer 3/4 Network Firewall traffic block kar raha hai.")
        print(f"[!] Diagnostic Reason: {e}")

if __name__ == "__main__":
    target_input = input("Audit karne ke liye Domain ya IP daalein (e.g., google.com): ").strip()
    if target_input:
        audit_multi_layer_firewall(target_input)