# 1.- Instalar el paquete en la consola
# pip install mysql-connector-python

# 2.- Importar la libreria
import mysql.connector

# 3.- Ejecutar el codigo de conexión con MySql

try:
    
    conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "",
        db = "bdscooby"
    )
    
    if conexion.is_connected():
        print("conexión exitosa")
        
        # Ejecutar el metodo cursor para recorrer
        # los resultados de mi base de datos
        cursor = conexion.cursor()
        
        # Ejecutar el script sql para obtener 
        # los datos de una tabla
        cursor.execute("SELECT * FROM amigos")
        
        # Almacenar todos los resultados de la 
        # tabla en una variable
        fila = cursor.fetchall()
        
        print(fila)
    
except Exception as error:
    print(error)