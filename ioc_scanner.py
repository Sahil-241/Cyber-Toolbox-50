import os

# Blacklist: Yahan wo files ya patterns daalein jinhe aap "suspicious" maante hain
SUSPICIOUS_FILES = ["malware.exe", "backdoor.py", "trojan.sh", "virus.bat"]

def scan_system(target_dir):
    print(f"--- Scanning directory: {target_dir} ---\n")
    found_count = 0
    
    # os.walk har sub-folder mein jaakar check karega
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # Check karein ki kya file ka naam blacklist mein hai
            if file in SUSPICIOUS_FILES:
                print(f"[!] ALERT: Suspicious file milti hai: {os.path.join(root, file)}")
                found_count += 1
            
            # Aap extension bhi check kar sakte hain (e.g., .exe wali files)
            elif file.endswith(".scr") or file.endswith(".vbs"):
                print(f"[?] CAUTION: Suspicious extension wali file: {os.path.join(root, file)}")
                found_count += 1

    print(f"\n[+] Scan complete. Total suspicious files found: {found_count}")

if __name__ == "__main__":
    path = input("Scan karne ke liye folder ka path dein: ")
    if os.path.exists(path):
        scan_system(path)
    else:
        print("Error: Yeh path exist nahi karta.")