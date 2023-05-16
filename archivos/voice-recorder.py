#Importamos los modulos necesarios
import sounddevice as sd
from scipy.io.wavfile import write
 
# Frecuencia
freq = 44100
 
# Duración de grabación
duration = 5
 
#Iniciamos la grabadora con la configuración asignada
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
 
# Esperamos el tiempo de grabación 
sd.wait()
 
#Guardamos el audio
write("audio-recorder.wav", freq, recording)

#Mensaje al terminar de guardar
print("Se guardo correctamente su grabación")
 