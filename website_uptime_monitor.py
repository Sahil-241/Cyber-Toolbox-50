import requests
import time
from datetime import datetime

# Input user se lena zyada behtar hai taaki baar-baar code na badalna pade
def get_status(url):
    # Agar user ne http/https nahi likha, toh add kar do
    if not url.startswith("http"):
        url = "https://" + url
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except:
        return "DOWN"

def monitor():
    # User se input lo
    target = input("Enter website URL to monitor (e.g., google.com): ")
    
    last_status = None
    print(f"\n[*] Monitoring started for: {target}")
    print(f"[*] Press Ctrl+C to stop.\n")

    while True:
        current_status = get_status(target)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if current_status != last_status:
            if current_status == 200:
                print(f"[{timestamp}] [+] STATUS CHANGE: {target} is UP! (200 OK)")
            else:
                print(f"[{timestamp}] [!] STATUS CHANGE: {target} is {current_status}!")
            
            last_status = current_status
        
        time.sleep(10)

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("\n[!] Monitoring stopped.")