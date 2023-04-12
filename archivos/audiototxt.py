# 1.- Instalar el paquete en la consola
# pip install SpeechRecognition

# 2.- Importar paquetes
import speech_recognition as sr

# 3.- Intancia del paquete
recognition = sr.Recognizer()

# 4.- Indicamos el path del audio
with sr.AudioFile('archivos/audio_english.wav') as source:
    audio = recognition.record(source)

    # 5.- Obtener texto del audio y 
    # escribirlo en un txt
    try:
        text = recognition.recognize_google(audio)
        
        file = open('archivos/texto.txt', 'w')
        file.write(text)
        file.close()
    except:
        print('Error, vuelve a intentar')