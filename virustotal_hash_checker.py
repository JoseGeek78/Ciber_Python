import hashlib
import requests
import os

# Obtener la clave API desde las variables de entorno para mayor seguridad
API_KEY = os.getenv("VT_API_KEY")  
URL = "https://www.virustotal.com/vtapi/v2/file/report"

def is_valid_hash(hash_value):
    """
    Verifica si el hash proporcionado es válido.
    VirusTotal soporta MD5 (32 caracteres), SHA1 (40 caracteres) y SHA256 (64 caracteres).
    """
    return len(hash_value) in [32, 40, 64] and all(c in "0123456789abcdefABCDEF" for c in hash_value)

def get_file_report(api_key, hash_value):
    """
    Consulta el informe de un archivo en VirusTotal usando su hash.
    
    Parámetros:
    - api_key: Clave API de VirusTotal.
    - hash_value: Hash del archivo que se quiere analizar.
    
    Retorna:
    - Un diccionario con el informe de VirusTotal si la consulta es exitosa.
    - None si ocurre algún error o el hash no tiene un informe disponible.
    """
    
    # Validar si el hash tiene una longitud correcta antes de hacer la solicitud
    if not is_valid_hash(hash_value):
        print("Error: El hash proporcionado no es válido.")
        return None
    
    # Parámetros para la solicitud a la API de VirusTotal
    params = {'apikey': api_key, 'resource': hash_value}
    
    try:
        # Realizar la solicitud HTTP GET con un tiempo de espera de 10 segundos
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()  # Lanza una excepción si hay errores HTTP
        
        # Convertir la respuesta en formato JSON
        data = response.json()
        
        # Verificar si VirusTotal tiene un informe para este hash
        if data.get("response_code") == 1:
            print(f"Resultado del análisis para {hash_value}:")
            print(f"Detecciones: {data.get('positives')} de {data.get('total')} motores de antivirus")
            return data
        else:
            print("No se encontró un informe para este hash en VirusTotal.")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return None

if __name__ == "__main__":
    # Solicitar al usuario que ingrese el hash del archivo
    hash_input = input("Ingrese el hash del archivo a verificar: ").strip()
    
    # Llamar a la función con el hash ingresado
    get_file_report(API_KEY, hash_input)
    