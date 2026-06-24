import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_single_port(target_host, port):
    try:
        # Create a TCP socket socket
        # AF_INET = IPv4, SOCK_STREAM = TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0) # 1 second timeout for speed
            
            # connect_ex returns 0 if connection was successful
            result = s.connect_ex((target_host, port))
            
            if result == 0:
                # Common ports name resolution mapping
                try:
                    service = socket.getservbyport(port, "tcp")
                except:
                    service = "Unknown Service"
                return port, service
    except Exception:
        pass
    return None

def run_port_monitor(target_host, start_port, end_port):
    print(f"\n--- [ Open Port Monitor Starting on: {target_host} ] ---")
    print(f"[+] Scanning ports from {start_port} to {end_port}...")
    print("[+] Identifying open TCP entry points, please wait...\n")
    
    open_ports = []
    
    # Fast multi-threaded tracking engine using ThreadPool
    # Max workers = 100 taaki network trace fatfat ho
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Submit all tasks to threads
        futures = {executor.submit(scan_single_port, target_host, port): port for port in range(start_port, end_port + 1)}
        
        print(f"{'PORT':<10} | {'STATUS':<12} | {'SERVICE NAME'}")
        print("-" * 45)
        
        for future in as_completed(futures):
            res = future.result()
            if res:
                port, service = res
                open_ports.append(port)
                print(f"{port:<10} | {'OPEN':<12} | {service}")
                
    print("\n================ [ MONITOR SUMMARY ] ================")
    print(f"[+] Scan Complete.")
    print(f"[+] Total Open Ports Uncovered: {len(open_ports)}")
    if open_ports:
        print(f"[!] Critical Notice: Ensure all open ports are authorized.")
    print("=====================================================")

if __name__ == "__main__":
    host = input("Scan karne ke liye Target IP ya Domain daalein (Local ke liye Enter dabayein): ").strip()
    if not host:
        host = "127.0.0.1" # Default to localhost (aapka apna computer)
        
    try:
        start_p = int(input("Start Port (e.g., 1): ") or 1)
        end_p = int(input("End Port (e.g., 1024): ") or 1024)
        
        run_port_monitor(host, start_p, end_p)
    except ValueError:
        print("[!] Invalide ports range. Restarting with default 1-1024...")
        run_port_monitor(host, 1, 1024)