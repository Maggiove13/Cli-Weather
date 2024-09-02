from dotenv import load_dotenv 
import requests
import os

def get_apikey():
    """Obtener la AI_key desde el archivo .env"""
    load_dotenv()
    API_key = os.getenv('API_key')
    return API_key

def get_weather(city):
    """Obtener la respuesta, el resultado de la URL de la API"""
    api_key = get_apikey()
    url =  f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response

