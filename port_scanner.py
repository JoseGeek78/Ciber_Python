import socket

TARGET = "192.168.1.1" # Cambia por la IP que quieras escanear
PORTS = [21, 22, 23, 80, 443, 3380] # Puertos a verificar

for port in PORTS:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1) # Tiempo máximo de espera
        if s.connect_ex((TARGET, port)) == 0:
            print(f"[+] Puerto {port} abiertp en {TARGET}")
        else:
            print(f"[-] Puerto {port} cerrado en {TARGET}")     
# Este script escanea los puertos especificados en la variable PORTS
# en la dirección IP especificada en TARGET.