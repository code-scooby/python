# 1.- Instalar el paquete en la consola
# pip install speedtest-cli

# 2.- Importamos la libreria
import speedtest

# 3.- Creamos una instancia de
# SpeedTest
red = speedtest.Speedtest()

# 4.- Imprimir en consola la velocidad
# de descarga y convertirla a Mbps
print(
    "Velocidad de Descarga:",
    round(
        red.download()/(1025*1025), 
        2),
    "Mbps"
)