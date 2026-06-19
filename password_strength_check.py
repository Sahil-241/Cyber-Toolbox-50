import re

def check_password_strength(password):
    """
    Analyzes password strength based on specific security criteria.
    """
    # Criteria definitions
    length_error = len(password) < 8
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    symbol_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Boolean logic for strength determination
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)
    
    if password_ok:
        return "STRONG", "Password meets all security complexity requirements."
    else:
        feedback = []
        if length_error: feedback.append("at least 8 characters")
        if digit_error: feedback.append("at least one digit (0-9)")
        if uppercase_error: feedback.append("at least one uppercase letter (A-Z)")
        if lowercase_error: feedback.append("at least one lowercase letter (a-z)")
        if symbol_error: feedback.append("at least one special character (!@#$... )")
        
        return "WEAK", f"Suggestions to improve: {', '.join(feedback)}"

def main():
    print("--- [ Password Strength Checker ] ---")
    pwd = input("Enter password to analyze: ")
    strength, feedback = check_password_strength(pwd)
    print(f"\nResult: {strength}")
    print(f"Details: {feedback}")

if __name__ == "__main__":
    main()