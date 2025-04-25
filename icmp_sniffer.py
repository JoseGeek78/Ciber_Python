from scapy.all import sniff, IP, ICMP, wrpcap
from collections import defaultdict

# Diccionario para contar tipos ICMP
icmp_counter = defaultdict(int)

# Lista para guardar los paquetes si se desea exportar a .pcap
captured_packets = []

def mostrar_paquete(pkt):
    """
    Función callback que se ejecuta por cada paquete capturado.
    Extrae y muestra información de los paquetes ICMP.
    """
    if IP in pkt and ICMP in pkt:
        ip_src = pkt[IP].src      # Dirección IP origen
        ip_dst = pkt[IP].dst      # Dirección IP destino
        icmp_type = pkt[ICMP].type  # Tipo de mensaje ICMP
        icmp_code = pkt[ICMP].code  # Código del mensaje ICMP

        # Contamos cada tipo de mensaje ICMP recibido
        icmp_counter[icmp_type] += 1

        # Guardamos el paquete si se desea guardar luego
        captured_packets.append(pkt)

        print(f"[ICMP] {ip_src} -> {ip_dst} | Type: {icmp_type}, Code: {icmp_code}")

# Parámetros de captura
TIMEOUT = 30   # Duración del sniffer (segundos)
MAX_PKTS = 50  # Número máximo de paquetes ICMP a capturar

print(f"Iniciando ICMP sniffer por {TIMEOUT} segundos o {MAX_PKTS} paquetes... (Ctrl+C para detener antes)")
sniff(filter="icmp", prn=mostrar_paquete, store=0, timeout=TIMEOUT, count=MAX_PKTS)

# Mostrar resumen de tipos ICMP capturados
print("\nResumen de tipos ICMP capturados:")
for icmp_type, count in icmp_counter.items():
    print(f" - Tipo {icmp_type}: {count} paquetes")

# Guardar en archivo pcap si se desea
SAVE_TO_PCAP = True
if SAVE_TO_PCAP and captured_packets:
    wrpcap("icmp_capturados.pcap", captured_packets)
    print("\nPaquetes guardados en 'icmp_capturados.pcap'")