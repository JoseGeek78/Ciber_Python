import os
import time
import logging

# Configuración del nombre del archivo de log a monitorear.
LOG_FILE = "var/log/auth.log"
# Palabra clave o patrón que se quiere detectar en el archivo. En este caso, indicamos "/etc/passwd".
ALERT_KEYWORD = "/etc/passwd"
# Configuración del logger
logging.basicConfig(
    filename='file_access.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

# Función para verificar si el archivo de log existe y es accesible.
def check_log_file():
    if not os.path.isfile(LOG_FILE):
        logger.error(f"El archivo de log {LOG_FILE} no existe o no es accesible.")
        return False
    return True
