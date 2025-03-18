import psutil

# Definir puertos estandar seguros
SAFE_PORTS = {22, 80, 443, 53}

# Iterar sobre las conexiones activas
for conn in psutil.net_connections(kind='inet'):
    laddr, raddr, status = conn.laddr, conn.raddr, conn.status
    
    # Si hay una dirección remota y el puerto no está en la lista segura
    if raddr and raddr.port not in SAFE_PORTS:
        print(f"[ALERTA] Conexión sospechosa")