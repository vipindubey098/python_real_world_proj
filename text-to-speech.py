import pyttsx3


# Creating an object for pyttsx3 class

engine = pyttsx3.init()

# see how many voice do we have in computer
for voice in engine.getProperty("voices"):
    print(voice)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) #here there was two voices in tutorial pc, 0 for first and 1 for second

# creating a function to convert text to speech 

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

# Ask the user to enter text

text = input("Enter your text now: ")

Speak(text)