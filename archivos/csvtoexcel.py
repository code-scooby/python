# 1.- Instalar el paquete en la consola
# pip install pandas
# pip install openpyxl

# 2.- Importar paquetes
import pandas as pd
import os

# 3.- Obtener el directorio actual
directorio = os.getcwd()

# 4.- Leer el archivo csv
csvDatos = pd.read_csv(
    directorio + '/archivos/username.csv'
)

# 5.- Convertir el csv a excel
csvDatos.to_excel(
    directorio + '/archivos/usernameconvertido.xlsx',
    index=False
)