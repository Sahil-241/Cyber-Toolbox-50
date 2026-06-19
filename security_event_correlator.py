import sys
from datetime import datetime

def analyze_live_event(event_log, state_db):
    ip = event_log["source_ip"]
    event = event_log["event_type"].upper()
    details = event_log["details"].lower()
    
    print(f"\n[+] Processing Event: {event} from {ip}...")
    
    # --- SECURITY RULE AUTOMATION ENGINE ---
    
    # RULE 1: Brute-Force Monitoring (Continuous Failures)
    if event == "AUTH_FAILURE":
        state_db["auth_failures"][ip] = state_db["auth_failures"].get(ip, 0) + 1
        print(f"[*] Current Auth Failure Count for {ip}: {state_db['auth_failures'][ip]}")
        
        if state_db["auth_failures"][ip] >= 3:
            print(f"\n[CRITICAL ALERT] Rule 1 Triggered: Potential Brute-Force Attack from IP {ip}!")
            print(f"    -> Action: Logged to Security Panel & IP flagged for monitoring.\n")

    # RULE 2: Correlation - Auth Success After Brute Force (Compromised Account)
    elif event == "AUTH_SUCCESS":
        if state_db["auth_failures"].get(ip, 0) >= 3:
            print(f"\n[CRITICAL CORRELATION] Rule 2 Triggered: ACCOUNT COMPROMISED!")
            print(f"    -> Warning: Successful login on {ip} immediately following {state_db['auth_failures'][ip]} failed attempts.")
            print(f"    -> Action: Revoking session tokens and forcing Multi-Factor Authentication (MFA).\n")
        
        state_db["login_state"][ip] = True
        # Reset auth failure on clean successful login if not already flag-triggered
        if state_db["auth_failures"].get(ip, 0) < 3:
            state_db["auth_failures"][ip] = 0

    # RULE 3: Complex Correlation - Unauthorized Data Exfiltration
    elif event == "NETWORK_OUTBOUND":
        if "gb" in details or "mb" in details:
            if state_db["login_state"].get(ip, False):
                print(f"\n[CRITICAL CORRELATION] Rule 3 Triggered: SUSPICIOUS DATA EXFILTRATION!")
                print(f"    -> Audit Trace: Authenticated session on {ip} is uploading high-volume data ({event_log['details']}).")
                print(f"    -> Action: Isolating host network adapter from production subnet.\n")
            else:
                print(f"\n[WARNING ALERT] Rogue Network Activity: Unauthenticated host {ip} transferring data ({event_log['details']}).\n")

def run_interactive_siem():
    print(f"\n--- [ Project 44: Live Security Event Correlator ] ---")
    print("[+] SIEM Engine Started. Monitoring local correlation pipelines...")
    
    # Core in-memory state databases
    state_db = {
        "auth_failures": {},
        "login_state": {}
    }
    
    while True:
        print("\n" + "="*50)
        print("Select Event Type to Inject:")
        print("1. AUTH_FAILURE     (Failed Login)")
        print("2. AUTH_SUCCESS     (Successful Login)")
        print("3. NETWORK_OUTBOUND  (Data Transfer)")
        print("4. Exit Tool")
        print("="*50)
        
        choice = input("Option select karein (1-4): ").strip()
        
        if choice == "4":
            print("[-] Shutting down SIEM Engine. Goodbye!")
            sys.exit()
            
        source_ip = input("Source IP address daalein (e.g., 192.168.1.50): ").strip() or "192.168.1.50"
        
        event_type = ""
        details = ""
        
        if choice == "1":
            event_type = "AUTH_FAILURE"
            details = "Invalid credential string for admin console"
        elif choice == "2":
            event_type = "AUTH_SUCCESS"
            details = "Session established for root user"
        elif choice == "3":
            event_type = "NETWORK_OUTBOUND"
            details = input("Kitna data transfer hua? (e.g., 10GB data backup, 50MB log): ").strip() or "5GB Data leaked"
        else:
            print("[!] Invalid choice! Please select correctly.")
            continue
            
        # Structure the live event block
        live_log = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "source_ip": source_ip,
            "event_type": event_type,
            "details": details
        }
        
        # Pass the event through the Correlation Rule Engine
        analyze_live_event(live_log, state_db)

if __name__ == "__main__":
    run_interactive_siem()