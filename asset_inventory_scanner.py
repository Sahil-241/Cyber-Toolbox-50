import os
import platform
import subprocess
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping_host(ip):
    current_os = platform.system().lower()
    
    # OS ke hisaab se ping command set karna
    # Windows par '-n 1', Linux/Kali par '-c 1'
    if current_os == "windows":
        command = ["ping", "-n", "1", "-w", "500", ip]
    else:
        command = ["ping", "-c", "1", "-W", "1", ip]
        
    try:
        # Run execution block without opening console window logs
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Return code 0 means host is active and responding
        if result.returncode == 0:
            # Try to resolve hostname if available
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unknown Hostname"
            return ip, "ACTIVE", hostname
    except Exception:
        pass
    return None

def run_inventory_scan(subnet_base):
    print(f"\n--- [ Asset Inventory Scanner Active ] ---")
    print(f"[+] Scanning network subnet range: {subnet_base}.1 to {subnet_base}.255")
    print("[+] Identifying live IT hardware assets, please wait...\n")
    
    active_assets = []
    
    print(f"{'IP ADDRESS':<18} | {'STATUS':<12} | {'HOSTNAME / DEVICE IDENTIFIER'}")
    print("-" * 65)
    
    # Thread pool wrapper to execute 50 pings simultaneously
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(ping_host, f"{subnet_base}.{i}"): i for i in range(1, 255)}
        
        for future in as_completed(futures):
            res = future.result()
            if res:
                ip, status, hostname = res
                active_assets.append((ip, hostname))
                print(f"{ip:<18} | {status:<12} | {hostname}")
                
    print("\n================ [ INVENTORY SUMMARY ] ================")
    print(f"[+] Network Discovery Scan Completed.")
    print(f"[+] Total Active Hardware Assets Found: {len(active_assets)}")
    print("=======================================================")

if __name__ == "__main__":
    print("Example Subnet Formats: 192.168.1 (Don't add the last dot or host ID)")
    subnet_input = input("Scan karne ke liye Subnet base daalein (e.g., 192.168.1): ").strip()
    
    if not subnet_input:
        # Default network gateway range check fallback
        subnet_input = "192.168.1"
        
    run_inventory_scan(subnet_input)