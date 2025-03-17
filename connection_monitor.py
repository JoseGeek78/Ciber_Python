import psutil

# Definir puertos estandar seguros
SAFE_PORTS = {22, 80, 443, 53}

# Iterar sobre las conexiones activas
for conn in psutil.net_connections(kind='inet'):
    