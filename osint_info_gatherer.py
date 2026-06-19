import socket
import requests
import dns.resolver  # pip install dnspython

def get_dns_records(domain):
    print("\n--- [ DNS Records ] ---")
    for record_type in ['A', 'MX', 'NS', 'TXT']:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            for rdata in answers:
                print(f"{record_type} Record: {rdata}")
        except:
            print(f"{record_type} Record: Not Found")

def gather_pro_info(domain):
    print(f"\n--- [ Pro OSINT Gathering for: {domain} ] ---")
    try:
        # IP Address
        ip = socket.gethostbyname(domain)
        print(f"[+] Primary IP: {ip}")
        
        # Geo-Location (Free API ka use)
        geo_data = requests.get(f"https://ipapi.co/{ip}/json/").json()
        print(f"[+] Location: {geo_data.get('city')}, {geo_data.get('country_name')}")
        
        # HTTP Headers & Security Check
        resp = requests.get(f"http://{domain}", timeout=5)
        print(f"[+] Web Server: {resp.headers.get('Server')}")
        
        # Security Header Check
        headers = resp.headers
        print(f"[+] X-Frame-Options: {headers.get('X-Frame-Options', 'Not Set')}")
        
        get_dns_records(domain)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = input("Target domain: ")
    gather_pro_info(target)