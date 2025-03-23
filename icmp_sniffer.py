from scapy.all import sniff, IP, ICMP

def detectar_ping(packet):
    if packet.haslayer(ICMP):
        print(f"[ALERTA] Ping detectado desde ")