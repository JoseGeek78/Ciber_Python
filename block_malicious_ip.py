import os
import platform
import reimport sys

MALICIOUS_IP = "111.111.1.111" # IP maliciosa a bloquear

# Ejecutar comando iptables para bloquear la IP
os.system(f"sudo iptables -A INPUT -s {MALICIOUS_IP} -j DROP")
print(f"[+] 1bloqueada la IP maliciosa: {MALICIOUS_IP}")
