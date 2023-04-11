# 1.- Instalar el paquete en la consola
# pip install moviepy

# 2.- Importar paquetes
import moviepy
import moviepy.editor

# 3.- Indicamos el path del video
video = moviepy.editor.VideoFileClip(
    'archivos/video.mp4')

# 4.- Extraemos el audio del video
audio = video.audio

# 5.- Guardamos el video
audio.write_audiofile('archivos/video.mp3')