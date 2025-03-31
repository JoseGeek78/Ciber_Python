import os
import psutilsutil

MALICIOUS_PROCESSV= "hacker_tool.exe"

for proc in psutil.process_iter(attrs={['name']}):
    if proc.info['name'] == MALICIOUS_PROCESS:
        print(f"Malicious process {MALICIOUS_PROCESS} detected!")
        os.system("shutdown /s /t 1")  # Shutdown the system immediately
        break
    else:
        print(f"Process {proc.info['name']} is safe.")
        continue
# This script checks for a specific malicious process and shuts down the system if found.
    