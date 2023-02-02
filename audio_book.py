#importing python modules
# PyPDF2 pip3 install PyPDF2
# pyttsx3 pip3 install pyttsx3

import PyPDF2
import pyttsx3

Engine = pyttsx3.init()
pdf_reader = PyPDF2.PdfFileReader(open("1T00145.pdf","rb"))
for page_num in range(pdf_reader.numPages):
    Text = pdf_reader.getPage(page_num).extractText()
    Engine.say(Text)
    Engine.save_to_file(Text, "audio.mp3")
    Engine.runAndWait()