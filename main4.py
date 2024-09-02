import argparse
from api import get_weather
from get_data import get_data
from error_handling import handle_api_errors, handle_general_errors
import json

# Función principal para ejecutar el programa
def main():
    parser = argparse.ArgumentParser(description="Aplicación CLI para consultar el clima.")
    parser.add_argument('-location', help='Consultar el clima según locación')
    parser.add_argument('-format', help='Elige el formato de salida: json, txt o csv', choices=['json', 'txt', 'csv'], default="txt")
    args = parser.parse_args()

    # Almacenamos los datos en las variables 
    city = args.location
    output_format = args.format
    
    try:
        resp = get_weather(city) # Obtenemos la respuesta de la API
        data = handle_api_errors(resp) # Convertimos la respuesta en formato json
        wheather = get_data(data) # Obtenemos la respuesta pero filtrada, con solo las infos que queremos mostrar

        # Imprimir datos del clima en el formato solicitado
        if output_format == 'json':
            print(json.dumps(wheather, indent=4))
        elif output_format == 'txt':
            for key, value in wheather.items():  # Usar d.items() para iterar sobre clave-valor
                print(f"{key}: {value}")
        elif output_format == 'csv':
            # Crear lista de claves y lista de valores
            keys = ",".join(wheather.keys())
            values = ",".join(str(value) for value in wheather.values())
            print(keys)
            print(values)
        else:
            print("Error: No se pudo completar la solicitud. Por favor intenta de nuevo más tarde.")
    except Exception:
        handle_general_errors()

if __name__ == "__main__":
    main()
