from scapy.all import sniff, IP, ICMP # Importamos las funciones necesarias de la librería Scapy

# Definimos una función que será ejecutada cada vez que se capture un paquete
def detectar_ping(packet):
    if packet.haslayer(ICMP): # Verificamos si el paquete tiene la capa ICMP (indicador de un ping)
        print(f"[ALERTA] Ping detectado desde {packet[IP].src}") # Mostramos una alerta con la IP de origen
        
sniff(filter="icmp", prn=detectar_ping, store=False)