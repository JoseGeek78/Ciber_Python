import os
import psutil

MALICIOUS_PROCESS= "hacker_tool.exe"

for proc in psutil.process_iter(attrs={['name']}):
    if proc.info['name'] == MALICIOUS_PROCESS:
        print("[ALERTA] Proceso malicioso detectado. Apagando el sistema...")
        os.system("shutdown /s /t 1")  # Para Windows
        # os.system("sudo shutdown -h now")  # Para Linux