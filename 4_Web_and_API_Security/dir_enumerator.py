import requests
import platform
import os

def clear_screen():
    # Detects OS and clears screen
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def dir_enumerator():
    clear_screen()
    print("==========================================")
    print("  Cyber-Toolbox-50: Directory Enumerator  ")
    print("==========================================")
    
    # 1. URL input aur auto-fix
    target = input("[+] Enter Domain (e.g., google.com): ")
    if not target.startswith("http"):
        url = "http://" + target
    else:
        url = target
        
    # 2. Wordlist path
    wordlist = input("[+] Enter Wordlist path (e.g., list.txt): ")
    
    print(f"\n[*] Starting scan on: {url}\n")
    
    try:
        with open(wordlist, 'r') as file:
            for line in file:
                word = line.strip()
                if not word: continue
                
                test_url = f"{url}/{word}"
                # Scan status display
                print(f"[*] Testing: {test_url}", end="\r") 
                
                try:
                    # Timeout rakha hai taaki slow sites par tool atke nahi
                    response = requests.get(test_url, timeout=2)
                    if response.status_code == 200:
                        print(f"\n[+] FOUND: {test_url} (Status: 200)")
                except:
                    # Connection errors ko ignore kar rahe hain
                    pass
        print("\n\n[*] Scan Completed.")
    except FileNotFoundError:
        print("\n[!] Error: Wordlist file nahi mili. Path check karo.")

if __name__ == "__main__":
    dir_enumerator()