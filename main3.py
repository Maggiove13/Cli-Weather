import requests
import argparse
from dotenv import load_dotenv
import os
import json

# Definir el archivo de cache
CACHE_FILE = 'cache.json'

# Cargar los datos del cache
def load_cache():
    try:
        with open(CACHE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Guardar los datos en el cache
def save_cache(cache):
    with open(CACHE_FILE, 'w') as file:
        json.dump(cache, file, indent=4)

# Función para obtener datos de la API
def get_weather_data(city, api_key):
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(URL)
    return response

# Función principal para procesar las ubicaciones
def main():
    # Cargar la clave API
    load_dotenv()
    API_key = os.getenv('API_key')

    if not API_key:
        print("Error: La clave API no está configurada. Por favor, asegúrate de que esté definida en tu archivo .env")
        return

    # Configurar los argumentos del CLI
    parser = argparse.ArgumentParser(description="Aplicación CLI para consultar el clima.")
    parser.add_argument('-locations', nargs='+', help='Lista de ubicaciones para consultar el clima (Ej: "Madrid-ES London-UK")', required=True)
    parser.add_argument('-format', help='Elige el formato de salida: json, txt o csv', choices=['json', 'txt', 'csv'], default='txt')
    args = parser.parse_args()

    locations = args.locations
    format_type = args.format

    # Cargar datos del cache
    cache = load_cache()

    # Procesar cada ubicación
    for location in locations:
        if location in cache:
            print(f"Datos del clima para {location} desde el cache:")
            print_data(cache[location], format_type)
        else:
            response = get_weather_data(location, API_key)
            if response.status_code == 200:
                data = response.json()
                cache[location] = data  # Guardar en el cache
                print(f"Datos del clima para {location} desde la API:")
                print_data(data, format_type)
            elif response.status_code == 401:
                print("Error: La clave API no es válida. Por favor verifica tu clave e intenta de nuevo.")
                return
            elif response.status_code == 404:
                print(f"Error: Ubicación {location} no encontrada. Por favor verifica la ortografía e intenta de nuevo.")
            else:
                print("Error: No se pudo completar la solicitud. Por favor intenta de nuevo más tarde.")

    # Guardar el cache actualizado
    save_cache(cache)

# Función para imprimir los datos según el formato
def print_data(data, format_type):
    if format_type == 'json':
        print(json.dumps(data, indent=4))
    elif format_type == 'txt':
        print(f"Clima en {data['name']}:\nTemperatura: {data['main']['temp']}°C\nCondiciones: {data['weather'][0]['description']}")
    # Nota: Implementar CSV si es necesario

# Ejecutar la función principal
if __name__ == "__main__":
    main()
