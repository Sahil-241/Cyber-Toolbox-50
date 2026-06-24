import os
import platform
import socket
import sys

def check_linux_compliance():
    report = []
    print("[+] Running Linux Compliance Checks...")
    
    # 1. Root User Check
    if os.getuid() == 0:
        report.append("[+] ROOT PRIVILEGES: Script running with elevated root privileges.")
    else:
        report.append("[WARNING] NON-ROOT: Running as standard user. Some system deep scans might be skipped.")
        
    # 2. Critical File Permission Check (/etc/shadow holds hashes)
    if os.path.exists("/etc/shadow"):
        mode = os.stat("/etc/shadow").st_mode & 0o777
        if mode <= 0o600:
            report.append("[+] FILE INTEGRITY: /etc/shadow permissions are secure.")
        else:
            report.append("[CRITICAL] VULNERABLE: /etc/shadow is world-readable! Strict permission fix required.")
            
    # 3. Common Vulnerable Ports (SSH, FTP)
    ports = [21, 22, 23]
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex(('127.0.0.1', port))
            if result == 0:
                report.append(f"[WARNING] OPEN PORT: Local Port {port} is open/listening. Verify service auth.")
                
    return report

def check_windows_compliance():
    report = []
    print("[+] Running Windows Compliance Checks...")
    
    # 1. Admin Privilege Check
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            report.append("[+] ADMIN RIGHTS: Script running with Full Administrative Token.")
        else:
            report.append("[WARNING] USER MODE: Running without Administrator privileges. UAC restriction active.")
    except:
        report.append("[-] Privilege check error.")
        
    # 2. Critical System Directory Access
    win_dir = os.environ.get('SystemRoot', 'C:\\Windows')
    if os.path.exists(win_dir):
        report.append(f"[+] DIRECTORY BASE: System Root found at {win_dir}.")
        
    # 3. Firewalls/Ports Basic Check
    ports = [135, 445, 3389] # RPC, SMB, RDP
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex(('127.0.0.1', port))
            if result == 0:
                report.append(f"[WARNING] EXPOSED ENDPOINT: Local Port {port} (SMB/RDP/RPC) is responsive.")
                
    return report

def run_compliance_audit():
    current_os = platform.system()
    print(f"\n--- [ Security Compliance Audit Hub | OS: {current_os} ] ---")
    
    if current_os == "Linux":
        audit_results = check_linux_compliance()
    elif current_os == "Windows":
        audit_results = check_linux_compliance() if os.name == 'posix' else check_windows_compliance()
    else:
        print(f"[-] OS {current_os} not explicitly mapped for deep audit.")
        return

    print("\n================ [ FINAL COMPLIANCE REPORT ] ================")
    for line in audit_results:
        print(line)
    print("=============================================================")

if __name__ == "__main__":
    run_compliance_audit()