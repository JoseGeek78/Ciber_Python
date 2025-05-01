#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP
import time
from threading import Timer

# Diccionario para almacenar los datos de SYN por IP: {ip: (contador, primer_timestamp)}
syn_data = {}

# Parámetros de configuración
THRESHOLD = 10  # Umbral de paquetes SYN para generar alerta
TIME_WINDOW = 10  # Ventana de tiempo en segundos en la que se evalúa el conteo


def check_syn_scans():
    """
    Función que se ejecuta periódicamente para revisar
    si alguna IP ha excedido el umbral de SYN dentro de la ventana.
    """
    current_time = time.time()
    expired_ips = []
    
    for ip, (count, first_time) in syn_data.items():
        elapsed = current_time - first_time
        
        if elapsed > TIME_WINDOW:
            expired_ips.append(ip)  # Marcar para eliminación
        elif count > THRESHOLD:
            print(f"ALERTA: Posible escaneo de puertos desde {ip} ({count} SYN en {elapsed:.2f} seg)")
    
    # Eliminar registros obsoletos
    for ip in expired_ips:
        del syn_data[ip]
    
    # Reprograma la verificación cada 5 segundos
    Timer(5, check_syn_scans).start()


def analizar_paquete(packet):
    """
    Función de callback que analiza cada paquete capturado.
    Detecta paquetes TCP con la bandera SYN activada y sin ACK.
    """
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_layer = packet[IP]
        tcp_layer = packet[TCP]
        
        # Detectar paquetes SYN: La bandera SYN equivale a 0x02
        if tcp_layer.flags & 0x02:
            src_ip = ip_layer.src
            now = time.time()
            
            if src_ip in syn_data:
                count, first_time = syn_data[src_ip]
                # Si el tiempo transcurrido supera la ventana, se reinicia el contador
                if now - first_time > TIME_WINDOW:
                    syn_data[src_ip] = (1, now)
                else:
                    syn_data[src_ip] = (count + 1, first_time)
            else:
                syn_data[src_ip] = (1, now)


# Iniciar el proceso de monitoreo
print("Iniciando detección de escaneos de puertos SYN...")
Timer(5, check_syn_scans).start()
sniff(filter="tcp", prn=analizar_paquete, store=False)