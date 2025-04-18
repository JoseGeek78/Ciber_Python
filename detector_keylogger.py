import os
import re

def detectar_keyloggers_en_carpeta(ruta_carpeta):
    sospechosos = []
    patrones_nombres = re.compile(r"(keylog|keyboard|hook)", re.IGNORECASE)
    
    for root, _, files in os.walk(ruta_carpeta):
        for archivo in files:
            if archivo.endswith(".py"):
                ruta_completa = os.path.join(root, archivo)
                try:
                    with open(ruta_completa, "r", encoding="utf-8", errors="ignore") as f:
                        contenido = f.read()
                    nombre_sospechoso = patrones_nombres.search(archivo)
                    contenido_sospechoso = re.search(r"(keyboard|pynput)", contenido)
                    if nombre_sospechoso or contenido_sospechoso:
                        sospechosos.append((ruta_completa, bool(nombre_sospechoso), bool(contenido_sospechoso)))
                except Exception as e:
                    print(f"Error leyendo {ruta_completa}: {e}")
    return sospechosos

if __name__ == "__main__":
    carpeta_a_escanear = input("Introduce la ruta de la carpeta a analizar: ").strip()
    if not os.path.isdir(carpeta_a_escanear):
        print("Ruta no válida o no existe.")
    else:
        resultados = detectar_keyloggers_en_carpeta(carpeta_a_escanear)
        if resultados:
            print("\nArchivos sospechosos detectados:")
            for ruta, nombre_flag, contenido_flag in resultados:
                print(f"- {ruta} | Nombre sospechoso: {nombre_flag} | Contenido sospechoso: {contenido_flag}")
        else:
            print("No se han encontrado archivos sospechosos.")
