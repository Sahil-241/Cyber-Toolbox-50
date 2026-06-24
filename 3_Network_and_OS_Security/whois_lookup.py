import whois
import platform
import os

def clear_screen():
    # Windows ke liye 'cls', Linux/Kali ke liye 'clear'
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_whois_info(domain):
    print(f"\n--- Searching WHOIS data for: {domain} ---\n")
    try:
        w = whois.whois(domain)
        
        # WHOIS data dictionary format mein hota hai
        print(f"[+] Registrar: {w.registrar}")
        print(f"[+] Creation Date: {w.creation_date}")
        print(f"[+] Expiration Date: {w.expiration_date}")
        print(f"[+] Name Servers: {w.name_servers}")
        print(f"[+] Status: {w.status}")
        print("-" * 40)
        
    except Exception as e:
        print(f"[!] Could not fetch WHOIS info: {e}")

def main():
    clear_screen()
    print("==========================================")
    print("      Cyber-Toolbox-50: WHOIS Lookup      ")
    print("==========================================")
    
    try:
        target = input("[+] Enter Domain: ")
        get_whois_info(target)
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    main()