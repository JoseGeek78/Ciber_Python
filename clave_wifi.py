import subprocess
import re

# Define el perfil de la red WiFi
perfil_red = "NOMBRE_DE_LA_RED"  # Cambia esto por el nombre real de la red

try:
    # Ejecuta el comando para obtener detalles del perfil
    resultado = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key=clear'],
                                        text=True, errors='backslashreplace')

    # Buscar la línea que contiene la contraseña
    match = re.search(r'Contenido de la clave\s*:\s*(.+)', resultado) or re.search(r'Key Content\s*:\s*(.+)', resultado)

    if match:
        print(f'La contraseña de la red "{perfil_red}" es: {match.group(1)}')
    else:
        print(f'No se pudo encontrar la contraseña para la red "{perfil_red}".')

except subprocess.CalledProcessError:
    print(f'No se pudo obtener la información del perfil "{perfil_red}". Verifica que el nombre sea correcto.')
except IndexError:
    print(f'El formato de salida no es el esperado para la red "{perfil_red}".')
