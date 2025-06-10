import shutil
import sys
import os

def main():
    # Se esperan dos parámetros: archivo de origen y número de copias
    if len(sys.argv) != 3:
        print("Uso: python {} <archivo_origen> <número_de_copias>".format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    
    archivo_origen = sys.argv[1]
    if not os.path.exists(archivo_origen):
        print(f"Error: El archivo '{archivo_origen}' no existe.")
        sys.exit(1)
    
    try:
        num_copias = int(sys.argv[2])
        if num_copias < 1:
            raise ValueError("El número de copias debe ser mayor o igual a 1.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    nombre_base, extension = os.path.splitext(archivo_origen)
    
    for i in range(1, num_copias + 1):
        destino = f"{nombre_base}_{i}{extension}"
        try:
            shutil.copy(archivo_origen, destino)
            print(f"Creado: {destino}")
        except Exception as error:
            print(f"Error al copiar {archivo_origen} a {destino}: {error}")
            sys.exit(1)

if __name__ == "__main__":
    main()  