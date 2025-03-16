import psutil

# Definir puertos estandar seguros
SAFE_PORTS = {22, 80, 443, 53}

# Iterar sobre las conexiones activas