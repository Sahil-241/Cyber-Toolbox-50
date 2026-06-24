import re
from urllib.parse import urlparse

def analyze_url(url):
    # Basic structural check: Agar protocol missing ho toh add karna
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
        
    print(f"\n--- [ Analyzing URL for Phishing Indicators: {url} ] ---")
    
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        path = parsed_url.path
        
        phishing_score = 0
        indicators = []
        
        # 1. IP Address Indicator: Asali brands URLs mein IP address nahi use karte
        ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        if ip_pattern.match(domain.split(':')[0]):
            phishing_score += 40
            indicators.append("[!] Direct IP Address used instead of a brand domain.")
            
        # 2. URL Length Indicator: Phishing links aksar tokens ya fake subdomains ki wajah se bade hote hain
        if len(url) > 75:
            phishing_score += 20
            indicators.append("[!] URL length is unusually long (>75 characters).")
            
        # 3. Suspicious Keywords Indicator: Fake login portals ko target karne wale words
        suspicious_words = ['login', 'verify', 'secure', 'update', 'banking', 'account', 'free', 'signin', 'wallet']
        found_words = [word for word in suspicious_words if word in url.lower()]
        if found_words:
            phishing_score += len(found_words) * 15
            indicators.append(f"[!] Suspicious keyword(s) detected: {', '.join(found_words)}")
            
        # 4. At Symbol (@) Indicator: URL mein '@' symbol use karke browser ko confuse kiya jata hai
        if "@" in url:
            phishing_score += 30
            indicators.append("[!] '@' symbol found. Used to mask the actual target domain.")
            
        # 5. Excessive Subdomains Indicator: Bohot saare dots (.) use karna
        dot_count = domain.count('.')
        if dot_count > 3:
            phishing_score += 20
            indicators.append(f"[!] High number of subdomains detected ({dot_count} subdomains).")

        # --- FINAL ANALYSIS REPORT ---
        print("\n================ [ ANALYSIS REPORT ] ================")
        if indicators:
            for ind in indicators:
                print(ind)
        else:
            print("[+] No common structural phishing markers detected.")
            
        print("-" * 53)
        print(f"[*] Threat Probability Score: {min(phishing_score, 100)}%")
        
        if phishing_score >= 60:
            print("[CRITICAL] Verdict: HIGH RISK. This link resembles a phishing pattern.")
        elif phishing_score >= 30:
            print("[WARNING] Verdict: MEDIUM RISK. Exercise caution before accessing.")
        else:
            print("[+] Verdict: LOW RISK. Structure appears normal.")
        print("=====================================================")
        
    except Exception as e:
        print(f"[!] Failed to parse URL: {e}")

if __name__ == "__main__":
    target_url = input("Check karne ke liye URL enter karein: ").strip()
    if target_url:
        analyze_url(target_url)
    else:
        print("[!] Default checking a simulated test URL...")
        analyze_url("http://192.168.1.1/secure-update/login.php?user=test")