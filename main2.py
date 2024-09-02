import requests
import argparse
from argparse import ArgumentParser, Namespace
from dotenv import load_dotenv
import os
import json


# Definir la función para obtener datos de la API
def get_api_data():
    # Cargar variables de entorno
    load_dotenv()
    API_key = os.getenv('API_key')

    # Verificar si la clave de API está presente
    if not API_key:
        print("Error: La clave API no está configurada. Por favor, asegúrate de que esté definida en tu archivo .env")
        return # Terminar la funcion

    # Instanciar la clase de Parser
    parser = ArgumentParser(description="Aplicación CLI para consultar el clima.")

    # Crear los comandos
    parser.add_argument('-location', help='Consultar el clima, según locación', required=True)
    parser.add_argument('-format', help='Elige el formato de salida: json, txt o csv', choices=['json', 'txt', 'csv'])
    args = parser.parse_args() # Acceder a lojs valores analizados
    city = args.location
    f = args.format

    # URL para la solicitud de la API
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'

    try:
        # Hacer la solicitud a la API
        response = requests.get(URL)

        # Verificar el código de estado de la respuesta
        if response.status_code == 401:
            print("Error: La clave API no es válida. Por favor verifica tu clave e intenta de nuevo.")
        elif response.status_code == 404:
            print("Error: Ubicación no encontrada. Por favor verifica la ortografía e intenta de nuevo.")
        elif response.status_code == 200:
            # Convertir la respuesta a formato JSON
            data = response.json()
            
            # Extraer datos de la respuesta
            coordenada = data ['coord']
            wheather = data ['weather'] # Acceder a la lista weather
            description = wheather[0]['description']
            main = data ['main'] # Dentro del diccionario main
            humidity = main['humidity']
            temp = main['temp']
            temp_min = main['temp_min']
            temp_max = main['temp_max']
            city_name = data ['name']
            sys = data ['sys'] # accede al diccionario sys
            country = sys['country']

            # En este diccionario se almaenará los datos de esa variable
            wheather = {
                'country': country,
                'city_name': city_name,
                'description': description,
                'humidity': humidity,
                'temp': temp,
                'temp_min': temp_min,
                'temp_max': temp_max
            }
            
            # Imprimir datos del clima en el formato solicitado
            if f == 'json':
                print(json.dumps(wheather, indent=4))
            elif f == 'txt':
                for key, value in wheather.items():  # Usar d.items() para iterar sobre clave-valor
                    print(f"{key}: {value}")
            # Implementar el formato CSV según sea necesario
            elif f == 'csv':
                # Crear lista de claves y lista de valores
                keys = ",".join(wheather.keys())
                values = ",".join(str(value) for value in wheather.values())
                print(keys)
                print(values)
        else:
            print("Error: No se pudo completar la solicitud. Por favor intenta de nuevo más tarde.")
    except Exception as e:
        print("Error: Algo salió mal. Verifica tu conexión e intenta de nuevo.")
        print(f"Detalles del error: {e}")

# Llamar a la función para obtener datos del clima
get_api_data()


