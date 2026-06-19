import sys

def calculate_risk_level(score):
    # Industry Standard Risk Matrix Scoring
    if score >= 15:
        return "CRITICAL", "🔴 Immediate action required! Isolate system and apply hotfix."
    elif score >= 10:
        return "HIGH", "🟠 High priority. Schedule remediation within 24-48 hours."
    elif score >= 5:
        return "MEDIUM", "🟡 Medium priority. Fix during the next maintenance cycle."
    else:
        return "LOW", "🟢 Low priority. Monitor and log behavior, patch routinely."

def run_risk_calculator():
    print(f"\n--- [ Project 46: Cyber Risk Assessment Calculator ] ---")
    print("[+] Framework: Quantitative & Qualitative Risk Matrix Automation")
    print("[+] Ready for asset risk evaluation...\n")
    
    while True:
        print("=" * 55)
        asset_name = input("Asset/Threat ka naam daalein (e.g., Web Server Ransomware) ya Exit ke liye 'q' dabayein: ").strip()
        if asset_name.lower() == 'q':
            print("[-] Shutting down Risk Calculator. Goodbye!")
            sys.exit()
            
        if not asset_name:
            print("[!] Asset name khali nahi ho sakta!")
            continue

        print("\n--- Likelihood Matrix (Attack hone ka kitna chance hai?) ---")
        print("1. Rare (Bohot kam chance)")
        print("2. Unlikely (Shayad hi ho)")
        print("3. Possible (Ho sakta hai)")
        print("4. Likely (Aamtaur par hota hai)")
        print("5. Almost Certain (Pakka hoga)")
        
        try:
            likelihood = int(input("Likelihood score select karein (1-5): "))
            if likelihood < 1 or likelihood > 5:
                print("[!] Score sirf 1 se 5 ke beech hona chahiye!")
                continue
        except ValueError:
            print("[!] Invalid input! Numeric value daalein.")
            continue

        print("\n--- Impact Matrix (Agar attack hua toh kitna nuksan hoga?) ---")
        print("1. Insignificant (Na ke barabar nuksan)")
        print("2. Minor (Chota-mota jhatka)")
        print("3. Moderate (Business par asar padega)")
        print("4. Major (Bada financial ya data loss)")
        print("5. Catastrophic (Business band hone ki naubat)")
        
        try:
            impact = int(input("Impact score select karein (1-5): "))
            if impact < 1 or impact > 5:
                print("[!] Score sirf 1 se 5 ke beech hona chahiye!")
                continue
        except ValueError:
            print("[!] Invalid input! Numeric value daalein.")
            continue

        # Core Mathematical Corelation: Risk = Likelihood x Impact
        risk_score = likelihood * impact
        risk_level, recommendation = calculate_risk_level(risk_score)

        print("\n================ [ RISK ASSESSMENT REPORT ] ================")
        print(f"[+] Targeted Asset/Threat : {asset_name}")
        print(f"[+] Likelihood Score     : {likelihood}/5")
        print(f"[+] Impact Score         : {impact}/5")
        print(f"[+] Total Risk Score     : {risk_score}/25")
        print(f"[+] RISK LEVEL STATUS    : {risk_level}")
        print(f"[+] Security Action      : {recommendation}")
        print("============================================================\n")

if __name__ == "__main__":
    run_risk_calculator()