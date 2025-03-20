import psutil

# Lista de procesos maliciosos conocidos
MALICIOUS_PROCESSES = {"malware.exe", "keylogger.py", "ransomware"}

for proc in psutil.process_iter(attrs=['pid', 'name']):
    