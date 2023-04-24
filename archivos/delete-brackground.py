# 1.- Instalar el paquete en la consola/terminal
#pip install rembg

# 2.- Importar las librerias
from rembg import remove
from PIL import Image
  
# 3.- Ruta de la imagen
input_path =  'scooby.jpg'
  
# 4.- Ruta de la imagen convertida
output_path = 'output.png'
  
# 5.- Procesando la imagen
input = Image.open(input_path)
  
# 6.- Removiendo el fondo
output = remove(input)
  
# 7.- Guardando la imagen
output.save(output_path)