import socket
import ssl
from urllib.parse import urlparse

def audit_ssl_tls(target_host):
    # Basic clean-up agar user poora URL daal de
    if "://" in target_host:
        target_host = urlparse(target_host).netloc
    
    print(f"\n--- [ SSL/TLS Configuration Audit: {target_host} ] ---")
    
    # Standard HTTPS port 443 hota hai
    port = 443
    context = ssl.create_default_context()
    
    try:
        print("[+] Connecting to target server over Port 443...")
        with socket.create_connection((target_host, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=target_host) as ssock:
                
                # Connection details nikalna
                version = ssock.version()
                cipher = ssock.cipher()
                cert = ssock.getpeercert()
                
                print("\n[+] Encryption Audit Results:")
                print(f"    - Active TLS Version   : {version}")
                print(f"    - Cipher Suite In Use  : {cipher[0]}")
                print(f"    - Encryption Strength  : {cipher[2]} bits")
                
                # Security Assessment (Rating)
                print("\n[+] Security Assessment:")
                if "TLSv1.3" in version:
                    print("    [!] Status: EXCELLENT! Server is using the latest TLS 1.3 protocol.")
                elif "TLSv1.2" in version:
                    print("    [!] Status: SECURE. TLS 1.2 is currently safe but consider upgrading to 1.3.")
                else:
                    print("    [WARNING] Status: VULNERABLE! Outdated TLS version detected. Risk of MitM attacks.")
                
                if cipher[2] < 128:
                    print("    [WARNING] Cryptographic Strength is weak (less than 128-bit).")
                else:
                    print("    [+] Cryptographic key strength is optimal.")
                    
    except ssl.SSLError as e:
        print(f"[-] SSL/TLS Handshake Failed: Protocol mismatch or self-signed certificate. Details: {e}")
    except Exception as e:
        print(f"[!] Connection Error: Could not connect to {target_host}. Details: {e}")

if __name__ == "__main__":
    target = input("Audit karne ke liye Website/Host daalein (e.g., google.com): ").strip()
    if target:
        audit_ssl_tls(target)
    else:
        print("[!] Input khali hai, default checking 'google.com'...")
        audit_ssl_tls("google.com")