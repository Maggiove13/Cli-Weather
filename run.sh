#!/bin/bash

# Comprobacion si el entorno virtual ya existe
if [ ! -d "venv" ]; then
  echo "Creando entorno virtual..."
  python -m venv venv
fi

# Activar el entorno virtual
source venv/bin/activate

# Instalar dependencias desde requirements.txt
echo "Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar la aplicacion con parametros predeterminados
echo "Ejecutando la aplicacion..."
python main4.py -location "Madrid" -format json

echo "-Script completado!"

