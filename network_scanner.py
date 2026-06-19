import nmap

def smart_scan(target_range):
    nm = nmap.PortScanner()
    # Note added here
    print("-" * 50)
    print("NOTE: Yeh tool sirf local network scan karta hai, public IP nahi.")
    print("-" * 50)
    print(f"[*] Scanning {target_range}... Please wait, this takes time.")
    
    nm.scan(hosts=target_range, arguments="-O -sV")
    
    for host in nm.all_hosts():
        print(f"\n--- Host: {host} ---")
        print(f"State: {nm[host].state()}")
        
        # OS Detection Logic
        if 'osmatch' in nm[host] and len(nm[host]['osmatch']) > 0:
            os = nm[host]['osmatch'][0]
            print(f"OS Detected: {os['name']} (Accuracy: {os['accuracy']}%)")
        else:
            print("OS: Pata nahi chala (Firewall protection).")

        # MAC Address aur Vendor Lookup
        if 'mac' in nm[host]['addresses']:
            mac = nm[host]['addresses']['mac']
            print(f"MAC Address: {mac}")
            
            if 'vendor' in nm[host] and mac in nm[host]['vendor']:
                print(f"Vendor: {nm[host]['vendor'][mac]}")
            else:
                print("Vendor: Unknown")

if __name__ == "__main__":
    network = input("Enter local network range (e.g., 10.197.227.0/24): ")
    try:
        smart_scan(network)
    except Exception as e:
        print(f"[!] Critical Error: {e}")