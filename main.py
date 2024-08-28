import requests
import argparse
from argparse import ArgumentParser, Namespace
from dotenv import load_dotenv
import os
import json

# Llamar a la función de load_dotenv para obtener la clave del API_key
load_dotenv()

# Instanciar la clase 
parser = ArgumentParser(description= "Aplicación CLI para consultar el clima.")

# Creando comandos
parser.add_argument('-location', help= 'Consultar el clima, segùn locación')
parser.add_argument('-format', help= 'elige el formato de salida', choices= ['json', 'txt', 'csv'])
args = parser.parse_args() # El método parse_args() analiza el argumento y devuelve un objeto que contiene los valores de los argumentos analizados.
city = args.location # Ahora es posible acceder a los valores de los argumentos analizados
f = args.format # Acceder a los valores del formato

# Aca visitamos la api para solicitar la info
API_key = os.getenv('API_key')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'
r = requests.get(url)

response = r.json() # Se recibirà la respuesta en formato json
# print(response)
# print(URL)

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
    'description': description,
    'humidity': humidity,
    'temp': temp,
    'temp_min': temp_min,
    'temp_max': temp_max,
    'city_name': city_name,
    'country': country
}

def data_type(d, f):
    if f == 'json':
        print(json.dumps(d, indent=4))
    elif f == 'txt':
        for key, value in d:
            print(f"{key}:{value}")
    elif f == 'csv':
        # Crear lista de claves y lista de valores
        keys = ",".join(d.keys())
        values = ",".join(str(value) for value in d.values())
        print(keys)
        print(values)

# result = "".join(str(key) + str(value) for key, value in dictionary.items())


data_type(data, f)


# print(json.dumps(data, indent=4)) ----> para darle formato json
