import requests
import platform
import os

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def detect_tech(url):
    if not url.startswith("http"):
        url = "http://" + url
    
    print(f"\n[*] Detecting technologies for: {url}...\n")
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        # Simple signature detection
        techs = []
        if 'Server' in headers:
            techs.append(f"Server: {headers['Server']}")
        if 'X-Powered-By' in headers:
            techs.append(f"Framework/Lang: {headers['X-Powered-By']}")
        if 'Set-Cookie' in headers and 'wp-' in headers['Set-Cookie']:
            techs.append("CMS: WordPress (Detected via Cookies)")
            
        if techs:
            for t in techs:
                print(f"[+] {t}")
        else:
            print("[-] No specific technologies detected in headers.")
            
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    clear_screen()
    print("==========================================")
    print("  Cyber-Toolbox-50: Tech Detector         ")
    print("==========================================")
    
    target = input("[+] Enter Domain: ")
    detect_tech(target)
    input("\n[+] Press Enter to exit...")

if __name__ == "__main__":
    main()