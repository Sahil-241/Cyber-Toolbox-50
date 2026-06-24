import hashlib

def generate_hash(text):
    """
    Input text ka SHA-256 hash generate karta hai.
    """
    # Text ko bytes mein convert karke hash generate karna
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def main():
    print("==========================================")
    print("--- [ Hash Generator & Verifier ] ---")
    print("==========================================")
    print("1. Generate Hash")
    print("2. Verify Data Integrity")
    
    choice = input("\nApna option chune (1/2): ")

    if choice == '1':
        data = input("\nString/Message enter karein jiska hash banana hai: ")
        result = generate_hash(data)
        print(f"\nGenerated SHA-256 Hash:\n{result}")
    
    elif choice == '2':
        data = input("\nOriginal data enter karein: ")
        stored_hash = input("Pehle ka stored hash enter karein: ")
        
        # Naye data ka hash generate karke purane se match karna
        new_hash = generate_hash(data)
        
        print(f"\nCalculated Hash: {new_hash}")
        
        if new_hash == stored_hash:
            print("\n[SUCCESS] Data Integrity Verified! Data mein koi badlav nahi hua.")
        else:
            print("\n[ALERT] Data Tampered! Hash match nahi hua. Data unsafe hai.")
    else:
        print("\n[ERROR] Invalid choice. Kripya 1 ya 2 chune.")

if __name__ == "__main__":
    main()