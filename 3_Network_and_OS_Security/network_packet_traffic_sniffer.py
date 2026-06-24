from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        
        # Protocol ka naam determine karna
        proto = "Other"
        if packet.haslayer(TCP):
            proto = "TCP"
            # Ports check karke exact protocol guess karna
            if packet[TCP].dport == 80 or packet[TCP].sport == 80: proto = "HTTP"
            elif packet[TCP].dport == 443 or packet[TCP].sport == 443: proto = "HTTPS"
            elif packet[TCP].dport == 21 or packet[TCP].sport == 21: proto = "FTP"
        elif packet.haslayer(UDP):
            proto = "UDP"
            if packet[UDP].dport == 53 or packet[UDP].sport == 53: proto = "DNS"
        elif packet.haslayer(ICMP):
            proto = "ICMP"

        # Table style output
        print(f"{proto:<10} | {src:<15} -> {dst:<15}")

print(f"{'PROTOCOL':<10} | {'SOURCE':<15} -> {'DESTINATION':<15}")
print("-" * 50)
sniff(prn=packet_callback, store=0)