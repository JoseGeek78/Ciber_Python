import subprocess

try:
    
    resultados = subprocess.check-output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key=clear'], shell=True).decode('utf-8', errors='backslashreplace')

    # Si el sistema es en inglés se pondrá 'Key Content'
    if 'Contenido de la clave' in resultados:
        for line in resultados.split('\n'):
            password = line.split(':')[1].strip()
            print(f'La contraseña de la red {perfil_red} es: {password}')
    else:
        print(f'No se pudo encontrar la contraseña para la red {perfil_red}')

except subprocess.CalledProcessError:
    print(f'No se pudo obtener la información del perfil {perfil_red}')