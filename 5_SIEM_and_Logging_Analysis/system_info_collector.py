import platform
import socket
import os

def collect_system_info():
    print(f"\n--- [ System Information Collector ] ---")
    
    try:
        # Operating System details
        print(f"[+] OS: {platform.system()} {platform.release()}")
        print(f"[+] Version: {platform.version()}")
        print(f"[+] Architecture: {platform.machine()}")
        print(f"[+] Processor: {platform.processor()}")
        
        # Network details
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"[+] Hostname: {hostname}")
        print(f"[+] Local IP: {ip_address}")
        
        # User details
        user = os.getlogin() if hasattr(os, 'getlogin') else "Unknown"
        print(f"[+] Current User: {user}")
        
    except Exception as e:
        print(f"[!] Error collecting system info: {e}")

if __name__ == "__main__":
    collect_system_info()