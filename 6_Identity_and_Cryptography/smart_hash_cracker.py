import hashlib
import itertools
import re
import sys
import time

def dynamic_analyzer_and_cracker(user_hash, max_brute_len=4):
    print(f"\n--- [ Project 49: Real Hybrid Hash Cracker ] ---")
    print(f"[+] Target Hash : {user_hash}")
    
    hash_len = len(user_hash)
    is_hex = bool(re.match(r"^[a-fA-F0-9]+$", user_hash))
    hash_type = "UNKNOWN"
    
    if hash_len == 32 and is_hex:
        hash_type = "md5"
    elif hash_len == 40 and is_hex:
        hash_type = "sha1"
    elif hash_len == 64 and is_hex:
        hash_type = "sha256"
        
    print(f"[+] Identified Algorithm : {hash_type.upper()}")
    if hash_type == "UNKNOWN":
        print("[!] Error: Yeh hash standard format (MD5/SHA1/SHA256) mein nahi hai!")
        return

    # --- STEP 1: INSTANT LOOKUP LIST ---
    local_db = {
        "565e317540234a9b6c00d6efeb067f92": "aA1",
        "cc00d6efeb067f92565e317540234a9b": "admin123",
        "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92": "123456"
    }
    
    clean_hash = user_hash.lower().strip()
    if clean_hash in local_db:
        print(f"\n🟢 [SUCCESS] Instant Match Found!")
        print(f"[+] Password : {local_db[clean_hash]}")
        return

    # --- STEP 2: INTELLIGENT BRUTE FORCE SEQUENCE (Agar list me na mile) ---
    print("\n[-] Hash instant list mein nahi mila.")
    print(f"[*] Launching Live Character Sequence Generator (Max Length: {max_brute_len})...")
    time.sleep(1)
    
    # Aapka bataya hua custom sequence order
    priority_chars = "aA1!bB@cC2#dD3$eE4%fF5^gG6&hH7*iI8(jJ9)kK0-lL_mM+nN=oO[pP]qQ{rR}sS;tT:uU'vV,wW.xX/yY?zZ"
    
    attempts = 0
    start_time = time.time()
    
    for length in range(1, max_brute_len + 1):
        for guess in itertools.product(priority_chars, repeat=length):
            word = "".join(guess)
            attempts += 1
            
            if hash_type == "md5":
                hashed = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "sha1":
                hashed = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == "sha256":
                hashed = hashlib.sha256(word.encode()).hexdigest()
                
            if hashed == clean_hash:
                duration = time.time() - start_time
                print(f"\n================ [ HASH CRACKED SUCCESS ] ================")
                print(f"[+] Password Found : {word}")
                print(f"[+] Total Attempts : {attempts}")
                print(f"[+] Time Taken     : {duration:.2f} seconds")
                print("==========================================================")
                return
                
    print(f"\n🔴 [FAILED] Di hui length limit ({max_brute_len}) tak password nahi mila.")

if __name__ == "__main__":
    h_input = input("Hash daalein: ").strip()
    try:
        # Aap jitna bada number doge, utne lambe password crack ho payenge
        length_limit = int(input("Max kitni length tak combinations check karein? (e.g., 3, 4 ya 5): "))
    except ValueError:
        length_limit = 4
        
    dynamic_analyzer_and_cracker(h_input, length_limit)