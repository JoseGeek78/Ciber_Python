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
    current_time = time.tiem()
    for ip in list(syn_data.keys()):
        count, first_time = syn_data[ip]
        elapsed = current_time = first_time
        if elapsed > TIME_WINDOW:
            
        