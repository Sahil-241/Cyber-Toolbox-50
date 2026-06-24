import os
import platform
import subprocess
import sys

def query_dns_txt(domain, record_prefix=""):
    current_os = platform.system().lower()
    target_query = f"{record_prefix}{domain}".strip()
    
    # OS according binary selection (Windows = nslookup, Linux = dig)
    if current_os == "windows":
        command = ["nslookup", "-type=TXT", target_query]
    else:
        command = ["dig", "TXT", target_query, "+short"]
        
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f"Error executing query: {e}"

def check_email_security(domain):
    print(f"\n--- [ Email Security Checker Active ] ---")
    print(f"[+] Inspecting Mail Spoofing Protection for: {domain}\n")
    
    # 1. Check SPF Record
    print("[*] Auditing SPF Record...")
    spf_raw = query_dns_txt(domain)
    has_spf = "v=spf1" in spf_raw.lower()
    
    if has_spf:
        print("    [PASS] SPF Record found! Authorized mail servers are restricted.")
        # Filter out the specific line for clean display
        for line in spf_raw.splitlines():
            if "v=spf1" in line.lower():
                print(f"    -> Log: {line.strip()}")
    else:
        print("    [FAIL] No SPF Record detected! Rogue servers can spoof this domain.")

    print("-" * 50)

    # 2. Check DMARC Record
    print("[*] Auditing DMARC Record...")
    dmarc_raw = query_dns_txt(domain, record_prefix="_dmarc.")
    has_dmarc = "v=dmarc1" in dmarc_raw.lower()
    
    if has_dmarc:
        print("    [PASS] DMARC Policy found! Instructions exist for spoofed emails.")
        for line in dmarc_raw.splitlines():
            if "v=dmarc1" in line.lower():
                print(f"    -> Log: {line.strip()}")
    else:
        print("    [FAIL] No DMARC Policy setup! Receiving servers won't know how to handle fakes.")

    print("-" * 50)

    # 3. DKIM Notice
    print("[*] DKIM (DomainKeys Identified Mail) Note:")
    print("    -> DKIM verification requires a specific selector (e.g., default._domainkey).")
    print("    -> Public cryptographic keys are appended automatically during live mail flow.")

    print("\n================ [ SECURITY SUMMARY ] ================")
    if has_spf and has_dmarc:
        print("🟢 STRONG PROTECTION: Spoofing risks minimized.")
    elif has_spf or has_dmarc:
        print("🟡 PARTIAL PROTECTION: Vulnerable to advanced brand phishing.")
    else:
        print("🔴 CRITICAL VULNERABILITY: High risk of Email Spoofing and domain hijack.")
    print("======================================================")

if __name__ == "__main__":
    target_domain = input("Scan karne ke liye Domain Name daalein (e.g., google.com): ").strip()
    if not target_domain:
        target_domain = "google.com"
        
    check_email_security(target_domain)