import hashlib
import os
import time

def calculate_file_hash(filepath):
    """File ka hash generate karta hai."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def main():
    print("--- [ File Integrity Monitor ] ---")
    filepath = input("Monitor karne ke liye file ka path enter karein: ")
    
    if not os.path.exists(filepath):
        print("File nahi mili!")
        return

    # Baseline hash set karna
    print(f"\n[INIT] Baseline hash set ho raha hai: {filepath}")
    original_hash = calculate_file_hash(filepath)
    print(f"Initial Hash: {original_hash}")
    
    print("\n[MONITORING] Monitoring chalu hai... (Ctrl+C dabayein rokne ke liye)")
    
    try:
        while True:
            time.sleep(2) # Har 2 second mein check karega
            current_hash = calculate_file_hash(filepath)
            
            if current_hash != original_hash:
                print(f"\n[ALERT!] File change detect hui hai!")
                print(f"Old Hash: {original_hash}")
                print(f"New Hash: {current_hash}")
                original_hash = current_hash # Update baseline
    except KeyboardInterrupt:
        print("\n[STOP] Monitoring band kar di gayi hai.")

if __name__ == "__main__":
    main()