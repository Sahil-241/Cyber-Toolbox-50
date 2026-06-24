import dns.resolver
import platform
import os

def clear_screen():
    # Windows ke liye 'cls', Linux/Kali ke liye 'clear'
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def dns_lookup(domain):
    records = ['A', 'MX', 'NS', 'TXT']
    print(f"\n--- DNS Records for {domain} ---\n")
    
    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"[{record} Records]")
            for rdata in answers:
                print(f" -> {rdata}")
            print("-" * 30)
        except:
            print(f"[{record} Records] -> Not found")
            print("-" * 30)

def main():
    clear_screen()
    print("==========================================")
    print("      Cyber-Toolbox-50: DNS Lookup        ")
    print("==========================================")
    
    try:
        target = input("[+] Enter Domain (e.g., google.com): ")
        dns_lookup(target)
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    main()