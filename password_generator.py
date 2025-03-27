import secrets
import string

def generar_password(longitud):
    if longitud < 4:
        raise ValueError("La longitud debe ser al menos 4 para incluir todos los tipos de caracteres.")

    # Seleccionar al menos un carácter de cada categoría.
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Para el resto, utilizar la combinación de todos los caracteres.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password += [secrets.choice(caracteres) for _ in range(longitud - 4)]

    # Mezclar la lista para no predecir la posición de los caracteres fijos.
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

print("Contraseña generada:", generar_password(12))
print("Contraseña generada:", generar_password(16))
print("Contraseña generada:", generar_password(20))