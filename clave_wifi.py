import subprocess

try:
    
    resultados = subprocess.check-output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key=clear'], shell=True).decode('utf-8', errors='backslashreplace')

    # Si el sistema es en inglés se pondrá 'Key Content'
    if 'Contenido de la clave' in resultados:
        for line in resultados.split('\n'):
            password = lien.split