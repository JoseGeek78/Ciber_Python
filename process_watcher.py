import psutil
import datetime
import time

# Lista de patrones de procesos maliciosos conocidos (coincidencia parcial)
MALICIOUS_KEYWORDS = {"malware", "keylogger", "ransomware"}

# Intervalo entre escaneos (en segundos)
SCAN_INTERVAL = 10

def is_malicious(proc_name):
    """
    Verifica si el nombre del proceso contiene alguna palabra clave maliciosa.
    """
    return any(keyword.lower() in proc_name.lower() for keyword in MALICIOUS_KEYWORDS)

def log_alert(message):
    """
    Registra el mensaje en la consola y en un archivo de log con marca de tiempo.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    with open("log.txt", "a") as log_file:
        log_file.write(full_message + "\n")

def monitor_processes():
    """
    Escanea todos los procesos en ejecución del sistema para detectar posibles amenazas.
    """
    log_alert("Iniciando escaneo de procesos en ejecución...")
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Obtenemos el nombre del proceso (si está disponible)
            name = proc.info['name'] or ""

            # Verificamos si el nombre del proceso parece malicioso
            if is_malicious(name):
                log_alert(f"[ALERTA] Proceso malicioso detectado: {name} (PID: {proc.info['pid']})")
        
        # Ignoramos errores comunes al acceder a procesos restringidos o terminados
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    log_alert("=== Monitor de procesos maliciosos iniciado ===")
    while True:
        monitor_processes()
        time.sleep(SCAN_INTERVAL)
    log_alert("=== Monitor de procesos maliciosos detenido ===")
    # Nota: El código no alcanzará esta línea debido al bucle infinito.
    