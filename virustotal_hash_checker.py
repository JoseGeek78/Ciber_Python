import hashlib
import requests
import os

API_KEY = os.getenv("VT_API_KEY")  # Obtener la clave API de las variables de entorno
URL = "https://www.virustotal.com/vtapi/v2/file/report"

def is_valid_hash(hash_value):
    """Check if the provided hash is valid (MD5, SHA1, SHA256)."""
    return len(hash_value) in [32, 40, 64] and all(c in "0123456789abcdefABCDEF" for c in hash_value)

def get_file_report(api_key, hash_value):
    """Fetch the file report from VirusTotal using the hash value."""
    if not is_valid_hash(hash_value):
        print("Error: The provided hash is not valid.")
        return None
    
    params = {'apikey': api_key, 'resource': hash_value}
    
    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("response_code") == 1:
            print(f"Scan result for {hash_value}: {data.get('positives')} detections out of {data.get('total')}")
            return data
        else:
            print("No report found for this hash.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    hash_input = input("Enter the hash of the file to check: ").strip()
    get_file_report(API_KEY, hash_input)
