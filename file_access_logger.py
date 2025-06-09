import os
import time
import logging

# Configuración del nombre del archivo de log a monitorear.
LOG_FILE = "/var/log/auth.log"
# Palabra clave o patrón que se quiere detectar en el archivo. En este caso, indicamos "/etc/passwd".
ALERT_KEYWORD = "/etc/passwd"

# Configuración del módulo logging para emitir mensajes en consola con diferentes niveles.
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s"
)

def monitor_logs():
    """
    Función para monitorizar en tiempo real el archivo de log.
    Lee continuamente el archivo y, si detecta en alguna línea la presencia del patrón
    de acceso sospechoso, emite una alerta.
    Además, detecta si el archivo ha sido rotado (por ejemplo, mediante logrotate).
    """
    try:
        # Abrir el archivo de log en modo lectura ('r')
        with open(LOG_FILE, "r") as f:
            # Posicionar el puntero al final para no procesar entradas antiguas.
            f.seek(0, os.SEEK_END)
            # Obtener el inodo del archivo para detectar cambios (rotación) en el log.
            current_inode = os.fstat(f.fileno()).st_ino
            
            while True:
                # Leer la siguiente línea del archivo.
                line = f.readline()
                
                # Si no se obtuvo ninguna línea nueva, espera un segundo antes de reintentar.
                if not line:
                    time.sleep(1)
                    
                    # Comprobar si el archivo ha sido rotado verificando el número de inodo.
                    try:
                        new_inode = os.stat(LOG_FILE).st_ino
                        if new_inode != current_inode:
                            logging.info("Rotación detectada en el archivo de log. Reabriendo el archivo...")
                            # Cerrar el archivo actual y reabrir el archivo actualizado.
                            f.close()
                            f = open(LOG_FILE, "r")
                            current_inode = os.fstat(f.fileno()).st_ino
                            # Posicionar el puntero al final del nuevo archivo para continuar.
                            f.seek(0, os.SEEK_END)
                    except FileNotFoundError:
                        # En caso de que el archivo no exista temporalmente, emitir advertencia y esperar.
                        logging.warning("Archivo de log no encontrado. Reintentando...")
                        time.sleep(1)
                    # Continuar con la siguiente iteración del bucle.
                    continue

                # Si la línea leída contiene la palabra clave de alerta, emitir una alerta.
                if ALERT_KEYWORD in line:
                    logging.warning(f"Acceso sospechoso detectado: {line.strip()}")
                    
    except Exception as e:
        # Manejo general de cualquier excepción que ocurra durante la monitorización.
        logging.error(f"Error al monitorear el archivo: {e}")

if __name__ == "__main__":
    # Ejecutar la función de monitorización cuando se invoque el script.
    monitor_logs()
# Este script monitoriza un archivo de log en tiempo real, buscando accesos sospechosos a un archivo específico.
# Se emiten alertas en caso de detectar accesos al archivo /etc/passwd.