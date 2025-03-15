#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP
import time
from threading import Timer

# Diccionario para almacenar los datos de SYN por IP: {ip: (contador, primer_timestamp)}
syn_data = {}

# Parámetros de configuración
THRESHOLD = 10  # Umbral de paquetes SYN para general alerta
TIME_WINDOW = 10  # Ventana de tiempo en segundos en la que se evalúa el conteo

def check_syn_scans():
    """
    Función que se ejecuta periódiamente para revisar 
    si alguna IP ha excedido el umbral de SYN dentro de la ventana.
    """
    current_time = time.time()
    for ip in list(syn_data.keys()):
        count, first_time = syn_data[ip]
        elapsed = current_time - first_time
        if elapsed > TIME_WINDOW:
            # Se elimina la ventana de tiempo si la IP ha expirado
        elif count > THRESHOLD:
            print(f"ALERTA: Posible escaneos de puertos desde {ip} ({count} SYN en {elapsed:.2f} seg)")
    # Reprograma la verificación cada 5 segundos
    Timer(5, check_syn_scans).start()

def analiar_paquete(packet):
    """
    Función de callback que analiza cada paquete capturado.
    Detecta paquetes TCP con la bandera SYN activada y sin ACK.
    """
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_layer = packet_getlayer(IP)
               