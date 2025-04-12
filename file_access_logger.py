import os
import time
import logging

# Configuración del nombre del archivo de log a monitorear.
LOG_FILE = "var/log/auth.log"
# Palabra clave o patrón que se quiere detectar en el archivo. En este caso, indicamos "/etc/passwd".
