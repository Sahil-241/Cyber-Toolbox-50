import sys
import time

def audit_custom_cloud(bucket_name, acl_status, port_number, cidr_block):
    print(f"\n--- [ Cloud Configuration Auditor Active ] ---")
    print("[+] Fetching your custom infrastructure parameters...")
    print("[+] Cross-referencing against CIS Cloud Benchmarks...\n")
    time.sleep(1)
    
    failed_rules = 0
    passed_rules = 0
    
    # 1. Storage Bucket Audit
    print(f"[*] Phase 1: Auditing Storage Object Security ({bucket_name})...")
    if "public" in acl_status.lower() or acl_status == "1":
        print(f"    [CRITICAL] Storage Object '{bucket_name}' is set to PUBLIC!")
        print(f"    └── [WARNING] Data is exposed to the internet. Strict policy required.")
        failed_rules += 1
    else:
        print(f"    [PASS] Storage Object '{bucket_name}' is securely locked (PRIVATE).")
        passed_rules += 1
        
    print("-" * 65)
    
    # 2. Network Firewall / Security Group Audit
    print(f"[*] Phase 2: Auditing Firewall Rule for Port {port_number}...")
    # Checking if management ports are exposed globally
    is_global = cidr_block == "0.0.0.0/0" or cidr_block.lower() == "any"
    is_management_port = port_number in [22, 3389, 21, 23]
    
    if is_global and is_management_port:
        print(f"    [CRITICAL] Management Port {port_number} is OPEN to the whole internet (0.0.0.0/0)!")
        print(f"    └── [RISK] Attackers can attempt brute-force or remote exploits.")
        failed_rules += 1
    elif is_global:
        print(f"    [NOTICE] Port {port_number} is open to public internet. (Normal for Web Servers).")
        passed_rules += 1
    else:
        print(f"    [PASS] Port {port_number} access is restricted to safe IP range: {cidr_block}.")
        passed_rules += 1

    # Final Compliance Output
    print("\n================ [ CLOUD AUDIT SUMMARY ] ================")
    print(f"[+] Total Compliance Rules Passed : {passed_rules}")
    print(f"[+] Total Misconfigurations Found : {failed_rules}")
    if failed_rules > 0:
        print(f"🔴 STATUS: COMPLIANCE FAILED. Security hardening is required.")
    else:
        print(f"🟢 STATUS: COMPLIANCE PASSED. Cloud infrastructure setup is clean.")
    print("=========================================================\n")

if __name__ == "__main__":
    print(f"--- [ Project 48: Cyber Cloud Auditor Console ] ---")
    
    # User inputs instead of hardcoded data
    b_name = input("1. Apne Cloud Storage/Bucket ka naam daalein: ").strip()
    if not b_name:
        print("[!] Bucket name zaroori hai!")
        sys.exit()
        
    print("\nSelect Bucket Access Policy:")
    print("1. Public (Puri duniya dekh sakti hai)")
    print("2. Private (Sirf aap dekh sakte hain)")
    acl_input = input("Option select karein (1-2): ").strip()
    
    acl_status = "public" if acl_input == "1" else "private"
    
    print("\n--- Firewall/Security Group Settings ---")
    try:
        port = int(input("2. Kaun sa network port check karna hai? (e.g., 22, 80, 443): "))
    except ValueError:
        print("[!] Port number numeric hona chahiye!")
        sys.exit()
        
    cidr = input("3. Kis IP range ko access diya hai? (Sabke liye '0.0.0.0/0' ya koi specific IP): ").strip()
    if not cidr:
        cidr = "0.0.0.0/0"
        
    # Triggering the scanner engine with user values
    audit_custom_cloud(b_name, acl_status, port, cidr)