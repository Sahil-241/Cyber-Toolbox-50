import ssl
import socket
import datetime
import platform
import os

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def check_ssl(hostname):
    port = 443
    print(f"\n[*] Checking SSL certificate for: {hostname}...\n")
    
    try:
        # SSL context banayein
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Certificate details extract karna
                subject = dict(x[0] for x in cert['subject'])
                issuer = dict(x[0] for x in cert['issuer'])
                
                print(f"[+] Issued to: {subject.get('commonName')}")
                print(f"[+] Issued by: {issuer.get('organizationName')}")
                print(f"[+] Version: {cert['version']}")
                print(f"[+] Valid from: {cert['notBefore']}")
                print(f"[+] Valid until: {cert['notAfter']}")
                
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    clear_screen()
    print("==========================================")
    print("   Cyber-Toolbox-50: SSL Cert Checker     ")
    print("==========================================")
    
    target = input("[+] Enter Domain (e.g., google.com): ")
    check_ssl(target)
    input("\n[+] Press Enter to exit...")

if __name__ == "__main__":
    main()