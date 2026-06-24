import os
import sys
import re

# External libraries ko check aur handle karne ke liye auto-installer logic
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("[!] 'requests' ya 'beautifulsoup4' library missing hai.")
    print("[+] Installing missing libraries automatically...")
    os.system(f"{sys.executable} -m pip install requests beautifulsoup4")
    import requests
    from bs4 import BeautifulSoup

def clear_screen():
    """Windows aur Linux dono me screen clear karne ke liye"""
    os.system('cls' if os.name == 'nt' else 'clear')

def scrape_and_find_role(url, staff_name):
    clear_screen()
    print(f"\n[+] Connecting to: {url}")
    
    # Standard Headers taaki website server requests ko block na kare (Universal User-Agent)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    # URL format checking (http:// ya https:// lagana zaroori hai)
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(f"[-] Website response error. Status Code: {response.status_code}")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Kachra tags ko filter out karna
        for script in soup(["script", "style", "noscript", "header", "footer"]):
            script.extract()
            
        text_content = soup.get_text()
        
        # Windows (\r\n) aur Linux (\n) dono ke line breaks ko properly handle karna
        lines = [line.strip() for line in text_content.splitlines() if line.strip()]
        
        print(f"[+] Searching for '{staff_name}' on the page...\n")
        found = False
        
        for i, line in enumerate(lines):
            # Regex match - Word boundaries ke sath takki accurate name search ho
            if re.search(r'\b' + re.escape(staff_name) + r'\b', line, re.IGNORECASE):
                found = True
                print("=" * 50)
                print(f"🎯 MATCH FOUND: {line}")
                print("=" * 50)
                print("Context / Role Details:")
                
                # Context lines nikalna (aaspas ka text)
                start = max(0, i - 1)
                end = min(len(lines), i + 3)
                for j in range(start, end):
                    prefix = "--> " if j == i else "    "
                    print(f"{prefix}{lines[j]}")
                print("=" * 50)
                
        if not found:
            print(f"[-] Sorry, '{staff_name}' is page par nahi mila.")
            print("[*] Tip: Kya aapne exact team/about page ka URL dala hai?")
            
    except requests.exceptions.ConnectionError:
        print("[-] Error: Internet connection check karein ya URL galat hai.")
    except Exception as e:
        print(f"[-] Ek unexpected error aayi: {e}")

if __name__ == "__main__":
    try:
        clear_screen()
        print("=== Universal Staff Directory Scraper ===")
        target_url = input("Website URL dalein (e.g., mysite.com/team): ").strip()
        name_to_search = input("Staff member ka naam dalein: ").strip()
        
        if target_url and name_to_search:
            scrape_and_find_role(target_url, name_to_search)
        else:
            print("[-] URL aur Naam dono daalna zaroori hai.")
            
    except KeyboardInterrupt:
        print("\n[-] Tool closed by user.")
        sys.exit()