import subprocess
import re

# Nombre del perfil de red Wi-Fi que deseas consultar
perfil_red = "NOMBRE_DE_LA_RED"  # Reemplaza por el nombre real de la red Wi-Fi

try:
    # Ejecuta el comando netsh para mostrar la información del perfil, incluyendo la clave en texto claro
    resultado = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', perfil_red, 'key=clear'],
        text=True,  # Decodifica automáticamente la salida a str en lugar de bytes
        errors='backslashreplace'  # Reemplaza caracteres no imprimibles en la salida (mejora compatibilidad)
    )

    # Busca la línea que contiene la contraseña (puede aparecer en español o inglés según el idioma del sistema)
    # Expresiones regulares tolerantes a espacio variable alrededor de los dos puntos
    match = re.search(r'Contenido\s+de\s+la\s+clave\s*:\s*(.+)', resultado, re.IGNORECASE) or \
            re.search(r'Key\s+Content\s*:\s*(.+)', resultado, re.IGNORECASE)

    if match:
        # Si se encuentra la contraseña, se imprime de forma clara
        print(f'🔐 La contraseña de la red "{perfil_red}" es: {match.group(1)}')
    else:
        # Si no se encuentra la clave, puede que el perfil no la tenga guardada o el idioma no fue detectado
        print(f'⚠️ No se pudo encontrar la contraseña para la red "{perfil_red}".')

except subprocess.CalledProcessError:
    # Este error ocurre si el comando falla, por ejemplo si el perfil no existe
    print(f'❌ No se pudo obtener la información del perfil "{perfil_red}". Verifica que el nombre sea correcto.')

except Exception as e:
    # Captura cualquier otro error inesperado (por ejemplo, error en ejecución o salida no estándar)
    print(f'⚠️ Ocurrió un error inesperado: {str(e)}')

