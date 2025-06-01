import os
import psutil
import logging

# Configuración del logger para registrar eventos de forma estructurada
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Nombre del proceso malicioso que se desea detectar
MALICIOUS_PROCESS = "hacker_tool.exe"

def shutdown_system():
    """
    Función para apagar el sistema de manera segura.
    - En Windows, se utiliza "shutdown /s /t 1".
    - En Linux y otros sistemas, se utiliza "sudo shutdown -h now".
    """
    try:
        if os.name == 'nt':  # Verifica si el sistema es Windows
            os.system("shutdown /s /t 1")
        else:  # Asume Linux u otros sistemas Unix-like
            os.system("sudo shutdown -h now")
    except Exception as e:
        logging.error("Error al intentar apagar el sistema: %s", e)

def detect_malicious_process(process_name):
    """
    Función que recorre todos los procesos en ejecución para detectar un proceso específico.
    
    Parámetros:
        process_name (str): El nombre del proceso que se considera malicioso.
    
    Retorna:
        bool: True si se detecta el proceso malicioso; de lo contrario, False.
    
    Se utiliza psutil.process_iter con el atributo 'name' para optimizar la búsqueda.
    Se manejan excepciones que puedan surgir al acceder a información de algunos procesos.
    """
    for proc in psutil.process_iter(['name']):
        try:
            # Compara el nombre del proceso actual (en minúsculas para evitar problemas con mayúsculas/minúsculas)
            if proc.info.get('name', '').lower() == process_name.lower():
                logging.warning("Proceso malicioso detectado: %s", proc.info.get('name'))
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            # Se captura si el proceso finaliza durante la iteración o si no se tienen los permisos necesarios
            logging.debug("No se pudo acceder a la información del proceso: %s", e)
    return False

def main():
    """
    Función principal que inicia la detección del proceso malicioso y, de encontrarse, procede a apagar el sistema.
    """
    logging.info("Iniciando la detección de procesos maliciosos...")
    if detect_malicious_process(MALICIOUS_PROCESS):
        logging.info("Procediendo al apagado del sistema debido a la detección de un proceso malicioso.")
        shutdown_system()
    else:
        logging.info("No se detectaron procesos maliciosos.")

if __name__ == "__main__":
    main()
