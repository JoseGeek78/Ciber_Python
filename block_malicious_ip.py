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

