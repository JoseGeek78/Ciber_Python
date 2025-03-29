import hashlib
import requests

API_KEY = "Tu_ API_KEY"  # Replace with your VirusTotal API key
HASH = "Tu_HASH"  # Replace with the hash you want to check
URL = "https://www.virustotal.com/vtapi/v2/file/report"

def get_file_report(api_key, hash_value):
    """Fetch the file report from VirusTotal using the hash value."""
    params = {
        'apikey': api_key,
        'resource': hash_value,
    }
    response = requests.get(URL, params=params)
    return response.json()

