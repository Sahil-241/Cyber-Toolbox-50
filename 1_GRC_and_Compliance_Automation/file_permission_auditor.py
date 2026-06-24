import os
import platform
import stat

def audit_linux_permissions(filepath):
    try:
        file_stat = os.stat(filepath)
        # Permissions nikalna (e.g., 0o777)
        permissions = file_stat.st_mode & 0o777
        
        # Check if file is World-Writable (kisi ke liye bhi writable hai)
        if permissions & stat.S_IWOTH:
            return f"[CRITICAL] World-Writable: {filepath} (Permissions: {oct(permissions)})"
        # Check if file is World-Readable
        elif permissions & stat.S_IROTH:
            return f"[WARNING] World-Readable: {filepath} (Permissions: {oct(permissions)})"
        return None
    except Exception:
        return None

def audit_windows_permissions(filepath):
    try:
        # Windows par hum check karenge ki kya file asani se modify ho sakti hai
        # os.access check karega ki current user session ke paas kya authority hai
        if os.access(filepath, os.W_OK):
            # Agar public location nahi hai aur writable hai toh report karenge
            if "Program Files" in filepath or "System32" in filepath:
                return f"[CRITICAL] Weak System File Permission: {filepath} (Writable by current session)"
            return f"[+] Accessible: {filepath} (Writable)"
        return None
    except Exception:
        return None

def run_permission_audit(target_directory):
    current_os = platform.system()
    print(f"\n--- [ File Permission Audit: {target_directory} | OS: {current_os} ] ---")
    print("[+] Scanning directory structure for weak access controls...\n")
    
    critical_count = 0
    warning_count = 0
    
    # Directory tree ko recursively walk karna
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            full_path = os.path.join(root, file)
            
            result = None
            if current_os == "Linux" or current_os == "Darwin":
                result = audit_linux_permissions(full_path)
            elif current_os == "Windows":
                result = audit_windows_permissions(full_path)
                
            if result:
                if "[CRITICAL]" in result:
                    critical_count += 1
                    print(result)
                elif "[WARNING]" in result:
                    warning_count += 1
                    print(result)

    print("\n================ [ AUDIT SUMMARY ] ================")
    print(f"[+] Total Critical Vulnerabilities Found : {critical_count}")
    print(f"[+] Total Warnings Found                : {warning_count}")
    print("====================================================")

if __name__ == "__main__":
    path_to_scan = input("Scan karne ke liye Directory Path daalein (e.g. . ya C:\\Test): ").strip()
    if not path_to_scan:
        path_to_scan = "." # Default current folder scan karega
        
    if os.path.exists(path_to_scan):
        run_permission_audit(path_to_scan)
    else:
        print("[!] Provided path does not exist!")