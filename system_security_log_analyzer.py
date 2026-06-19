import re

def analyze_logs(file_path):
    # Sirf critical security keywords aur Windows Event IDs (4625 = Failed Login)
    # 4625 bahut zaruri hai hacking attempts pakadne ke liye
    critical_patterns = [r"failed", r"error", r"unauthorized", r"denied", r"4625"]
    
    print(f"\n{'='*60}")
    print(f"[*] Analyzing Log File: {file_path}")
    print(f"{'='*60}\n")
    
    found_any = False
    
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                # Check agar line mein koi bhi critical pattern hai
                if any(re.search(p, line, re.IGNORECASE) for p in critical_patterns):
                    # Faltu ki cheezein ignore karo (jaise TPM/Time-service jo tumhe pareshan kar rahi thi)
                    if not any(ignore in line for ignore in ["TPM", "Time-Service", "Information"]):
                        print(f"[!] SECURITY ALERT [Line {line_num}]: {line.strip()}")
                        found_any = True
        
        if not found_any:
            print("[+] Koi suspicious activity nahi mili, log file saaf hai!")
            
    except FileNotFoundError:
        print("[!] Error: File nahi mili, path sahi se daalo.")
    except Exception as e:
        print(f"[!] Unexpected Error: {e}")

if __name__ == "__main__":
    path = input("Enter log file path: ").replace('"', '') # path mein quotes ho toh remove kar dega
    analyze_logs(path)