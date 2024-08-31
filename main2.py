import requests
import argparse
from argparse import ArgumentParser, Namespace
from dotenv import load_dotenv
import os
import json


# Definir la función para obtener datos de la API
def get_api_data():
        # Llamar a la función de load_dotenv para obtener la clave del API_key
    load_dotenv()
    API_key = os.getenv('API_key')

    # Instanciar la clase 
    parser = ArgumentParser(description= "Aplicación CLI para consultar el clima.")

    # Creando comandos
    parser.add_argument('-location', help= 'Consultar el clima, según locación')
    parser.add_argument('-format', help= 'elige el formato de salida: json, txt o csv', choices= ['json', 'txt', 'csv'])
    args = parser.parse_args() # El método parse_args() analiza el argumento y devuelve un objeto que contiene los valores de los argumentos analizados.
    city = args.location # Ahora es posible acceder a los valores de los argumentos analizados
    f = args.format # Acceder a los valores del formato que el usuario quiera

    
    # # Aca visitamos la api para solicitar la info a la api
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'

        # Extraer datos de la respuesta
    coordenada = response['coord']
    wheather = response['weather'] # Acceder a la lista weather
    description = wheather[0]['description']
    main = response['main'] # Dentro del diccionario main
    humidity = main['humidity']
    temp = main['temp']
    temp_min = main['temp_min']
    temp_max = main['temp_max']
    city_name = response['name']
    sys = response['sys'] # accede al diccionario sys
    country = sys['country']

    # En este diccionario se almaenará los datos de esa variable
    data = {
        'country': country,
        'city_name': city_name,
        'description': description,
        'humidity': humidity,
        'temp': temp,
        'temp_min': temp_min,
        'temp_max': temp_max
    }
    
    try:
        # Hacer la solicitud a la API
        response = requests.get(URL)
        # Convertir la respuesta a formato JSON
        data = response.json()

        # Verificar el código de estado de la respuesta
        if response.status_code == 401:
            print("Error: La clave API no es válida. Por favor verifica tu clave e intenta de nuevo.")
        elif response.status_code == 404:
            print("Error: Ubicación no encontrada. Por favor verifica la ortografía e intenta de nuevo.")
        elif response.status_code == 200:
            # Imprimir datos del clima en el formato solicitado
            if f == 'json':
                print(json.dumps(data, indent=4))
            elif f == 'txt':
                print(f"Clima en {data['name']}:\nTemperatura: {data['main']['temp']}°C\nCondiciones: {data['weather'][0]['description']}")
            # Nota: Implementación del formato CSV depende de requerimientos específicos
        else:
            print("Error: No se pudo completar la solicitud. Por favor intenta de nuevo más tarde.")
    except Exception as e:
        print("Error: Algo salió mal. Verifica tu conexión e intenta de nuevo.")
        print(f"Detalles del error: {e}")

# Llamar a la función para obtener datos del clima
get_api_data()


