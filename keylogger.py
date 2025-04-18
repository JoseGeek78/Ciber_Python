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

