import psutil

# Definir un conjunto de puertos considerados como seguros (puertos comunes de servicios legítimos)
SAFE_PORTS = {22, 80, 443, 53}  # SSH, HTTP, HTTPS, DNS

def main():
    print("[*] Escaneando conexiones activas...\n")
    
    try:
        # Iterar sobre todas las conexiones de red tipo INET (IPv4 e IPv6)
        for conn in psutil.net_connections(kind='inet'):
            laddr = conn.laddr if conn.laddr else None  # Dirección local
            raddr = conn.raddr if conn.raddr else None  # Dirección remota
            status = conn.status  # Estado de la conexión (ESTABLISHED, LISTEN, etc.)
            
            # Verificamos si hay dirección remota y si el puerto remoto no es seguro
            if raddr and raddr.port not in SAFE_PORTS:
                print(f"[ALERTA] Conexión sospechosa detectada:")
                print(f"  - Dirección local: {laddr.ip}:{laddr.port}")
                print(f"  - Dirección remota: {raddr.ip}:{raddr.port}")
                print(f"  - Estado: {status}\n")

    except PermissionError:
        print("[ERROR] Permisos insuficientes para acceder a las conexiones. Ejecuta como administrador o root.")
    except Exception as e:
        print(f"[ERROR] Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
