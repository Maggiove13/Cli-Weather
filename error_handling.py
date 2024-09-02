# Manejo de errores de la API

def handle_api_errors(response):
    """Manejar errores de la API"""
    if response.status_code == 401:
        print("Error: La clave API no es válida. Por favor verifica tu clave e intenta de nuevo.")
    elif response.status_code == 404:
        print("Error: Ubicación no encontrada. Por favor verifica la ortografía e intenta de nuevo.")
    elif response.status_code != 200:
        print("Error: No se pudo completar la solicitud. Por favor intenta de nuevo más tarde.")
    else:
        # No hay error, retornar los datos
        return response.json()
    
    # Retornar None si hubo un error
    return None

# Función para manejar errores generales
def handle_general_errors(error):
    """Manejar errores generales"""
    print("Error: Algo salió mal. Verifica tu conexión e intenta de nuevo.")
    print(f"Detalles del error: {error}")
