# 1.- Instalamos paquete 
# pip install cryptography

# 2.- Importamos paquetes
from cryptography.fernet import Fernet
from PIL import Image

# 3.- Generamos una llave 
key = Fernet.generate_key()
fernet = Fernet(key)

# 4.- Indicamos el archivo a cifrar
image = Image.open("audio/scooby.jpg")

# 5.- Convertimos la imagen a bytes 
# y la encriptamos
image_bytes = image.tobytes()
encrypted_bytes = fernet.encrypt(image_bytes)

# 6.- Guardamos la imagen
with open("audio/scooby-cifrado.jpg", "wb") as file:
    file.write(encrypted_bytes)
    
# 7.- Desencriptamos la imagen
decryted_bytes = fernet.decrypt(encrypted_bytes)
decryted_image = Image.frombytes(image.mode, image.size, decryted_bytes)

# 8.- Guardamos la imagen desencriptadas
decryted_image.save("audio/scooby-descifrado.jpg")