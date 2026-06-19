import whois
from datetime import datetime

def monitor_domain_expiry(domain_name):
    print(f"\n--- [ Domain Expiry Monitor: {domain_name} ] ---")
    
    try:
        print("[+] Fetching WHOIS records from global registry...")
        domain_info = whois.whois(domain_name)
        
        # Dono dates ko alag-alag nikalna
        creation_date = domain_info.creation_date
        expiry_date = domain_info.expiration_date
        
        # Agar dates list format mein aati hain toh pehla element uthana
        if isinstance(creation_date, list): creation_date = creation_date[0]
        if isinstance(expiry_date, list): expiry_date = expiry_date[0]
            
        if expiry_date:
            print(f"[+] Registrar: {domain_info.registrar}")
            # YAHA PAR CORRECTION HAI: Ab dono alag print hongi
            print(f"[+] Creation Date: {creation_date.strftime('%Y-%m-%d') if hasattr(creation_date, 'strftime') else creation_date}")
            print(f"[+] Expiry Date: {expiry_date.strftime('%Y-%m-%d') if hasattr(expiry_date, 'strftime') else expiry_date}")
            
            # Remaining days calculation
            if isinstance(expiry_date, datetime):
                today = datetime.now()
                remaining_days = (expiry_date - today).days
                
                if remaining_days < 0:
                    print(f"[!] STATUS: EXPIRED! (Expired {abs(remaining_days)} days ago)")
                elif remaining_days <= 30:
                    print(f"[!] STATUS: CRITICAL! Only {remaining_days} days left for renewal.")
                else:
                    print(f"[+] STATUS: SECURE ({remaining_days} days remaining before expiry)")
            else:
                print("[-] Could not automatically parse days remaining due to date format.")
        else:
            print("[-] Expiry date not found in public registry.")
            
    except Exception as e:
        print(f"[!] Error reading domain data: {e}")

if __name__ == "__main__":
    target = input("Monitor karne ke liye Domain Name daalein (e.g., google.com): ").strip()
    if target:
        domain = target.replace("https://", "").replace("http://", "").replace("www.", "").split("/")[0]
        monitor_domain_expiry(domain)
    else:
        monitor_domain_expiry("google.com")