import requests
import platform
import os

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_headers(url):
    # Auto-fix: http:// add karna
    if not url.startswith("http"):
        url = "http://" + url
    
    print(f"\n[*] Fetching headers for: {url}\n")
    
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        print("--- HTTP Headers ---\n")
        for key, value in headers.items():
            print(f"{key}: {value}")
            
    except requests.exceptions.RequestException as e:
        print(f"[!] Could not connect to the server: {e}")

def main():
    clear_screen()
    print("==========================================")
    print("  Cyber-Toolbox-50: HTTP Header Analyzer  ")
    print("==========================================")
    
    target = input("[+] Enter Domain: ")
    get_headers(target)
    input("\n[+] Press Enter to exit...")

if __name__ == "__main__":
    main()