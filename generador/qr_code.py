# 1.- Instalar el paquete en la consola
# pip install qrcode

# 2.- Importamos la libreria
import qrcode

# 3.- Indicamos el contenido del QR
img = qrcode.make('https://linktr.ee/codescooby')

# 4.- Guardamos la imagen
img.save('generador/linktree.png')