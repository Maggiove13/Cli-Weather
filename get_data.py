# Obtener los datos de la API y de ellos clasificar cuales se mostraran


def get_data(data):
    """Extraer los datos de la respuesta"""

    weather_info = data.get(
        "weather", [{}]
    )  # Utiliza [{}] como valor predeterminado para evitar errores
    description = weather_info[0].get("description", "No disponible")
    main = data.get("main", {})
    humidity = main.get("humidity", "No disponible")
    temp = main.get("temp", "No disponible")
    temp_min = main.get("temp_min", "No disponible")
    temp_max = main.get(
        "temp_max", "No disponible"
    )  # si el valor no esta entonces no disponible que no pueda tirar un mensaje none, sino será No
    city_name = data.get("name", "No disponible")
    sys = data.get("sys", {})
    country = sys.get("country", "No disponible")

    # En este diccionario se almacenarán los datos del clima extraídos, filtrados los que quisiera mostrar
    weather_data = {
        "country": country,
        "city_name": city_name,
        "description": description,
        "humidity": humidity,
        "temp": temp,
        "temp_min": temp_min,
        "temp_max": temp_max,
    }

    return weather_data
