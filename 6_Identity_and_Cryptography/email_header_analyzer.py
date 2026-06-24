import email
from email import policy
from email.parser import BytesParser

def analyze_header(file_path):
    try:
        with open(file_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        
        print("\n--- [ Email Header Analysis ] ---")
        print(f"Subject: {msg['subject']}")
        print(f"From: {msg['from']}")
        print(f"To: {msg['to']}")
        print(f"Date: {msg['date']}")
        print(f"Return-Path: {msg['return-path']}")
        
        # Received fields show the path the email took
        print("\n[!] Received Hops:")
        for header, value in msg.items():
            if header.lower() == 'received':
                print(f" -> {value}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    path = input("Email header file ka path dein (.eml file): ")
    analyze_header(path)