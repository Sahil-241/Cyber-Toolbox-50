import datetime
import os

def generate_report(target, findings):
    """
    Ek formatted security report generate karta hai.
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Security_Report_{target.replace('.', '_')}_{timestamp}.txt"
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write("="*40 + "\n")
            file.write("       SECURITY AUDIT REPORT       \n")
            file.write("="*40 + "\n")
            file.write(f"Target Domain/IP: {target}\n")
            file.write(f"Report Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("-"*40 + "\n\n")
            
            file.write("DETAILED FINDINGS:\n")
            for i, finding in enumerate(findings, 1):
                file.write(f"{i}. [!] {finding}\n")
            
            file.write("\n" + "="*40 + "\n")
            file.write("End of Report\n")
            
        print(f"\n[SUCCESS] Report ban gayi hai: {os.path.abspath(filename)}")
        
    except Exception as e:
        print(f"\n[ERROR] Report generate karne mein samasya aayi: {e}")

def main():
    print("--- [ Security Report Generator Pro ] ---")
    target = input("Target ka naam (Domain/IP): ").strip()
    
    if not target:
        print("Target name khali nahi ho sakta!")
        return

    print("Apni findings enter karein (khatam karne ke liye 'done' likhein):")
    
    findings_list = []
    while True:
        entry = input("> ").strip()
        if entry.lower() == 'done':
            print("[+] Findings record ho gayi hain. Report generate ho rahi hai...")
            break
        elif entry == "":
            continue
        else:
            findings_list.append(entry)
            print(f"    [Added]: {entry}") 
            
    if findings_list:
        generate_report(target, findings_list)
    else:
        print("Koi finding nahi di, report nahi banegi.")

if __name__ == "__main__":
    main()