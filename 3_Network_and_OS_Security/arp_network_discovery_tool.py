from scapy.all import ARP, Ether, srp

def scan_network(target_ip):
    # ARP Request Packet: Hum network mein pooch rahe hain "Kaun kaun online hai?"
    print(f"[*] Scanning range: {target_ip}...")
    
    # ARP packet create karna
    arp = ARP(pdst=target_ip)
    
    # Ethernet frame create karna (Broadcast karne ke liye)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Packet ko combine karna
    packet = ether / arp
    
    # Packet bhejna aur jawab ka wait karna
    # srp() function Layer 2 par packets bhejta hai
    result = srp(packet, timeout=3, verbose=0)[0]
    
    # Jawab (Response) ko process karna
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

if __name__ == "__main__":
    # User se range mangna
    ip_range = input("Enter Network Range (e.g., 10.197.227.0/24): ")
    
    # Scanner chalana
    discovered_devices = scan_network(ip_range)
    
    # Output table format mein dikhana
    print("-" * 50)
    print(f"{'IP ADDRESS':<20} | {'MAC ADDRESS'}")
    print("-" * 50)
    
    if discovered_devices:
        for device in discovered_devices:
            print(f"{device['ip']:<20} | {device['mac']}")
    else:
        print("[!] Koi device nahi mila. (Admin rights check karo!)")