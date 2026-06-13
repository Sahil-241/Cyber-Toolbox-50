import requests
from collections import Counter

def analyze_infrastructure(domain):
    print(f"\n[!] Analyzing infrastructure for: {domain}...")
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            lines = response.text.splitlines()
            subdomain_map = {} # {subdomain: ip}
            ip_list = []

            for line in lines:
                parts = line.split(',')
                if len(parts) == 2:
                    sub, ip = parts[0], parts[1]
                    subdomain_map[sub] = ip
                    ip_list.append(ip)

            # IP frequency analyze karo (Kaunsa IP sabse zyada use ho raha hai)
            ip_counts = Counter(ip_list)
            common_ip = ip_counts.most_common(1)[0][0] # Main server IP

            print(f"\n[+] Main Infrastructure IP: {common_ip}")
            print("-" * 40)

            for sub, ip in subdomain_map.items():
                status = " (Normal)"
                if ip != common_ip:
                    status = " [!] VULNERABILITY ALERT: Divergent IP detected!"
                print(f"{sub} -> {ip}{status}")
        
        else:
            print("[!] Could not connect to API.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    target = input("Enter Target Domain: ")
    analyze_infrastructure(target)