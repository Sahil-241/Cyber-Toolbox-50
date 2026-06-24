import socket
import ssl # SSL/TLS ke liye (Port 443 ke liye zaroori)

def grab_http_banner(ip, port):
    try:
        # socket banaya
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        
        # Agar port 443 hai toh SSL context wrap karna padega
        if port == 443:
            context = ssl.create_default_context()
            s = context.wrap_socket(s, server_hostname=ip)
        
        s.connect((ip, port))
        
        # HTTP Request bheji (server ko bolne par majboor karne ke liye)
        request = f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n"
        s.send(request.encode())
        
        # Banner/Response receive kiya
        response = s.recv(2048)
        print(f"    [+] HTTP Banner: {response.decode().splitlines()[0]}")
        s.close()
    except Exception as e:
        print(f"    [!] Could not grab HTTP banner: {e}")

def auto_banner_grabber(ip):
    common_ports = [21, 22, 80, 443] # Main ports
    print(f"\n[!] Scanning open ports for: {ip}...")
    
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            print(f"\n[+] Port {port} is OPEN!")
            if port in [80, 443]:
                grab_http_banner(ip, port)
            else:
                # Baki ports ke liye standard grab
                try:
                    print(f"    [+] Banner: {s.recv(1024).decode().strip()}")
                except:
                    print("    [!] No standard banner received.")
        s.close()

if __name__ == "__main__":
    target_ip = input("Enter Target IP: ")
    auto_banner_grabber(target_ip)