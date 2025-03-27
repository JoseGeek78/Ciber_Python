import random
import string

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for i in range(longitud))
    return password

print("Contraseña generada: ", generar_password(12))
# Esta función genera una contraseña aleatoria de longitud 12 utilizando letras mayúsculas, minúsculas, dígitos y caracteres especiales.

