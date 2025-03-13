#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP
import time
from threading import Timer

# Diccionario para almacenar los datos de SYN por IP: {ip: (contador, primer_timestamp)}
syn_data = {}

# Parámetros de configuración
THRESHOLD = 10  # Umbral de paquetes SYN para general alerta
TIME_WINDOW = 10  # Ventana de tiempo en segundos en la que se evalúa el conteo

