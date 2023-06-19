#import pypdf and gtts
from pypdf import PdfReader
from gtts import gTTS

#create reader
reader = PdfReader("pdf-text.pdf")

#get number of pages
number_of_pages = len(reader.pages)

#select page to extract the text
page = reader.pages[0]

#extract text
text = page.extract_text()

#convert text to audio
tts = gTTS(text, lang='es-us')

#save audio in format mp3
tts.save("pdf-audio.mp3")
