# 1.- Instalar pip install pytube

# 2.- Importar la libreria
from pytube import YouTube

# 3.- Link del video a descargar
yt = YouTube('https://www.youtube.com/watch?v=BBGEG21CGo0&ab_channel=UkesofHazzard')

# 4.- Indicamos el formato en .mp4
# y descargamos el video
yt.streams.filter(
            progressive=True,
            file_extension='mp4'
            ).first().download()