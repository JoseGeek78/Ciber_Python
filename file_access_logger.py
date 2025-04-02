import os
import time

LOG_FILE = "/var/log/auth.log"

def monitor_logs():
    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line and "/etc/passwd" in line:
                print(f"[ALERTA] Acceso sospechoso detectado: {line.strip()}")
            time.sleep(1)

monitor_logs()
