import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor

def check_link(target_url, base_url):
    try:
        # User-Agent add kiya hai taaki kuch websites bot samajh kar block na karein
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.head(target_url, timeout=5, allow_redirects=True, headers=headers)
        
        link_type = "Internal" if urlparse(base_url).netloc == urlparse(target_url).netloc else "External"
        
        if res.status_code >= 400:
            print(f"[!] BROKEN [{link_type}]: {target_url} -> Status: {res.status_code}", flush=True)
        else:
            print(f"[+] WORKING [{link_type}]: {target_url} -> Status: {res.status_code}", flush=True)
            
    except Exception as e:
        print(f"[!] UNREACHABLE: {target_url} -> Error: {e}", flush=True)

def run_pro_scan(url):
    if not url.startswith("http"): url = "http://" + url
    print(f"\n--- [ Starting Detailed Threaded Scan: {url} ] ---")
    
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        links = {urljoin(url, link.get('href')) for link in soup.find_all('a') if link.get('href')}
        
        print(f"[+] Total unique links to scan: {len(links)}")
        print("-" * 50)
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            for link in links:
                executor.submit(check_link, link, url)
                
    except Exception as e:
        print(f"[!] Critical Error: {e}")

if __name__ == "__main__":
    target = input("Website URL: ")
    run_pro_scan(target)