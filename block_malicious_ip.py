import os
import platform
import re
import sys

# Dirección IP maliciosa a bloquear (puedes cambiarla dinámicamente)
MALICIOUS_IP = "111.111.1.111"

# Verificamos que estamos ejecutando esto en un sistema Linux
if platform.system() != "Linux":
    print("[X] Este script solo puede ejecutarse en sistemas Linux.")
    sys.exit(1)
    
# Validación sencilla de fortmato de IPv4
if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", MALICIOUS_IP):
    print("[X] Dirección IP inválida.")
    sys.exit(1)
    
# Comando para bloquear la IP maliciosa usando iptables
command = f"sudo iptables -A INPUT -s {MALICIOUS_IP} -j DROP"

# Ejecutamos el comando con os.system (puedes usar subprocess también para mayor control)
exit_code = os.system(command)

# Comprobamo si se ejecutó correctamente
if exit_code == 0:
    print(f"[+] Dirección IP {MALICIOUS_IP} bloqueada exitosamente.")
else:
    print(f"[X] Error al bloquear la dirección IP {MALICIOUS_IP}.")
    sys.exit(1)
