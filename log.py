#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP
import time
from threading import Timer

# Diccionario para almacenar los datos de SYN por IP: {ip: (contador, primer_timestamp)}
syn_data = {}

