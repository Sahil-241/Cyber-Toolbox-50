import requests

def get_vendor(mac_address):
    # API URL
    url = f"https://api.macvendors.com/{mac_address}"
    
    try:
        # API call karna
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            return f"[+] Vendor: {response.text}"
        elif response.status_code == 404:
            return "[!] Error: Vendor nahi mila (Invalid MAC address)."
        else:
            return "[!] Error: Server se connection nahi ho raha."
            
    except Exception as e:
        return f"[!] Connection Error: {e}"

if __name__ == "__main__":
    print("-" * 50)
    print("NOTE: Ye tool sirf local network/internet device ka vendor lookup karta hai.")
    print("-" * 50)
    
    mac = input("Enter MAC Address (e.g., 00:1A:2B:3C:4D:5E): ")
    result = get_vendor(mac)
    print(result)