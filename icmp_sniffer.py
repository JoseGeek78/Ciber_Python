from scapy.all import sniff, IP, ICMP # Importamos las funciones necesarias de la librería Scapy

# Definimos una función que será ejecutada cada vez que se capture un paquete
def detectar_ping(packet):
    if packet.haslayer(ICMP):
        print(f"[ALERTA] Ping detectado desde {packet[IP].src}")
        
sniff(filter="icmp", prn=detectar_ping, store=False)