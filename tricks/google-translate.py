#Run command: pip install deep_translator
#Import library 
from deep_translator import GoogleTranslator

#Text to translate
text_translate = 'I want to translate this text'

#Language to translate
lang = "es"

#Google translate instance
google_translator = GoogleTranslator(source='auto', target=lang)

#Translate text to the chosen language
translated = google_translator.translate(text_translate)

#Print result
print(translated)
