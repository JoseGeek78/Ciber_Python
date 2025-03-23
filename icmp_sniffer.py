from scapy.all import sniff, IP, ICMP # Importamos las funciones necesarias de la librería Scapy


def detectar_ping(packet):
    if packet.haslayer(ICMP):
        print(f"[ALERTA] Ping detectado desde {packet[IP].src}")
        
sniff(filter="icmp", prn=detectar_ping, store=False)