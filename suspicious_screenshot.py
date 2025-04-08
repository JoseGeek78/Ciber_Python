import pyautogui    # Importa la librería que permite capturar pantallas
import psutil       # Importa la librería que permite obtener información de procesos del sistema

# Lista de nombres de procesos sospechosos. Se utiliza una lista para facilitar la comparación.
MALICIOUS_PROCESSES = [
    "snifre.exe", "sniffer.exe", "sniffer", 
    "snif.exe", "sniff.exe", "sniff", 
    "sniffler.exe", "sniffler"
]

# Itera sobre todos los procesos del sistema, obteniendo información de PID y nombre
for proc in psutil.process_iter(['pid', 'name']):
    try:
        # Se obtiene el nombre del proceso en minúsculas para evitar discrepancias por mayúsculas/minúsculas
        process_name = proc.info['name'].lower() if proc.info['name'] else ""
        # Compara si el nombre del proceso coincide con alguno de los nombres en la lista sospechosa
        if process_name in (name.lower() for name in MALICIOUS_PROCESSES):
            print(f"[ALERTA] Proceso sospechoso detectado: {proc.info['name']} (PID: {proc.info['pid']})")

            # Captura una captura de pantalla de la situación actual
            screenshot = pyautogui.screenshot()
            # Define un nombre de archivo incluyendo el PID del proceso para facilitar su identificación
            filename = f"suspicious_process_{proc.info['pid']}.png"
            # Guarda la captura en el archivo especificado
            screenshot.save(filename)
            print(f"Captura de pantalla guardada como {filename}")

            # Se detiene el bucle tras detectar el primer proceso sospechoso
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # En caso de no poder acceder a la información del proceso, se ignora y se continúa con el siguiente
        continue
else:
    # Este bloque se ejecuta solo si el bucle se completa sin haber realizado break (sin encontrar procesos sospechosos)
    print("No se encontraron procesos sospechosos.")
