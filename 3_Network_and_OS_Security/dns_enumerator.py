import dns.resolver

def dns_enumerator(domain):
    print(f"\n--- [ DNS Enumeration for: {domain} ] ---")
    
    # DNS records ke types jo hum scan karenge
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
    
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n[+] {record} Records:")
            for data in answers:
                print(f"    -> {data.to_text()}")
        except Exception:
            # Agar koi record nahi milta toh error skip karein
            print(f"\n[+] {record} Records: Not Found")

if __name__ == "__main__":
    # Library install karne ke liye: pip install dnspython
    target = input("Scan karne ke liye domain enter karein: ")
    dns_enumerator(target)