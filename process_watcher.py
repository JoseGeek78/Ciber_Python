import psutil

# Lista de procesos maliciosos conocidos
MALICIOUS_PROCESSES = {"malware.exe", "keylogger.py", "ransomware"}

for proc in psutil.process_iter(attrs=['pid', 'name']):
    if proc.info['name'] in MALICIOUS_PROCESSES:
        print(f"[ALERTA] Proceso malicioso detectado: {proc.info['name']} (PID: {proc.info['pid']})")
        