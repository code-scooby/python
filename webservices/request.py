# 1.- Instalar un paquete en la consola / terminal -> pip install requests

# 2.- Importar
import json
import requests

# 3.- Copiar la ruta de la API
url = "https://rickandmortyapi.com/api/character/1"

# 4.- Obtener con requests toda la información de la API
response = requests.get(url)

# 5.- Almacenar los datos en una variable y parsear a JSON
data = response.json()

print(data["name"])