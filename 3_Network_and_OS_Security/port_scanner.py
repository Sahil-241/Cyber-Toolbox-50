import socket
import threading
from concurrent.futures import ThreadPoolExecutor
import time

# Socket settings
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

def main():
    target = input("Enter target IP: ")
    print(f"\n--- Scanning all 65536 ports on: {target} ---")
    start_time = time.time()
    
    # Max 200 threads ek sath chalenge (Safe for Windows/Linux)
    with ThreadPoolExecutor(max_workers=200) as executor:
        for port in range(1, 65536):
            executor.submit(scan_port, target, port)
            
    print(f"\nScan completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()